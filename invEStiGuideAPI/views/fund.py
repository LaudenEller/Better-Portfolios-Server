"""View module for handling requests for funds"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from invEStiGuideAPI.models.fund import Fund
from invEStiGuideAPI.models.recommendation import Recommendation
from invEStiGuideAPI.models.watch import WatchedSecurity
from invEStiGuideAPI.serializers.fund_serializer import FundSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import action
from invEStiGuideAPI.serializers.recommendation_serializer import RecommendationSerializer
from invEStiGuideAPI.serializers.watched_serializer import WatchListSerializer
from django.contrib.auth.models import User
from django.db.models import Q

class FundView(ViewSet):
    
    # get all funds
    def list(self, request):
        """Handles GET requests for all funds
        
        Returns:
            Response -- JSON serialized list of funds
        """
        
        funds = Fund.objects.all()
        
        #  asset_classes // query string = "/funds?assetclass=<asset_class id>"
        asset_class = request.query_params.get('assetclass', None)
        if asset_class is not None:
            funds = funds.filter(asset_class_id=asset_class)
                    
        # countries // query string = "/funds?country=<country id>"
        country = request.query_params.get('country', None)
        if country is not None:
            funds = funds.filter(country_id=country)
            
        # industries // query string = "/funds?industry=<industry id>"
        industry = request.query_params.get('industry', None)
        if industry is not None:
            funds = funds.filter(industry_id=industry)
            
        # issuers // query string = "/funds?issuer=<issuer id>"
        issuer = request.query_params.get('issuer', None)
        if issuer is not None:
            funds = funds.filter(issuer_id=issuer)
            
        # esg_concerns // query string = "/funds?esg=<esg_concern id>,<esg_concern id>,<esg_concern id>"
            # Returns all funds with a matching esg_concern
        esg = request.query_params.get('esg', None)
        if esg is not None:
            esg = self.request.GET.get("esg", "")
            esg_values = esg.split(",")
            funds = funds.filter(esg_concern__in=esg_values)
            
        # search for a fund // query string = "/funds?name=<string>"
        #   Returns funds who's name begins with search text
        search_text_name = self.request.query_params.get('name', None)
        if search_text_name is not None:
                funds = funds.filter(
                    Q(name__startswith=search_text_name)
                )
        
        serializer = FundSerializer(funds, many=True)
        return Response(serializer.data)

    #  get a fund
    def retrieve(self, request, pk):
        """Handles GET requests for a fund
        
        Returns:
            Response -- JSON serialized fund
        """
        
        try:
            fund = Fund.objects.get(pk=pk)
            serializer = FundSerializer(fund)
            return Response(serializer.data)
        except ObjectDoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    # Watch a fund
    @action(methods=['POST'], detail=True)
    def watch(self, request, pk):
        """Handles adding a fund to the current user's watch list"""
        
        fund = Fund.objects.get(pk=pk)
        w_fund = WatchedSecurity.objects.create(
            fund=fund,
            user=request.auth.user
        )
        serializer = WatchListSerializer(w_fund)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # Unwatch a fund
    @action(methods=['DELETE'], detail=True)
    def unwatch(self, request, pk):
        """Handles removing a fund from the current user's watch list"""
        
        fund = Fund.objects.get(pk=pk)
        user = User.objects.get(pk=request.auth.user.id)
        w_fund = WatchedSecurity.objects.get(user=user, fund=fund)
        w_fund.delete()
        return Response({'message': 'Fund removed from watch list'}, status=status.HTTP_204_NO_CONTENT)
    
    # Get the current user's watch list
    @action(methods=['GET'], detail=False)
    def watchlist(self, request):
        """Handles requests for a users watch list"""
        
        try:
            funds = Fund.objects.filter(watchedsecurity__user_id=request.auth.user.id)
            serializer = FundSerializer(funds, many=True)
            return Response(serializer.data)
        except (Fund.DoesNotExist) as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    # Get the current user's list of recommendations
    @action(methods=['GET'], detail=False)
    def reclist(self, request):
        """Handles requests for the current user's recommendation list"""
        
        recs = Recommendation.objects.filter(
            Q(recommendee=request.auth.user))
        serializer = RecommendationSerializer(recs, many=True)
        return Response(serializer.data)
    
    # Recommend a fund
    @action(methods=['POST'], detail=False)
    def rec(self, request):
        try:
            if request.method == "POST":
                fund = Fund.objects.get(pk=request.data['fundId'])
                recommendee = User.objects.get(pk=request.data['user'])
                recommendation, _ = Recommendation.objects.get_or_create(
                    note=request.data['note'],
                    fund=fund,
                    recommender=request.auth.user,
                    recommendee=recommendee
                )
                serializer = RecommendationSerializer(recommendation)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except (Fund.DoesNotExist, User.DoesNotExist) as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)