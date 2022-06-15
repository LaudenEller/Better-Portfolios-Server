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
from invEStiGuideAPI.serializers.recommednation_serializer import RecommendationSerializer
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

        # add query parameters for:
        #  asset_classes // query string = "/funds?assetclass=<asset_class id>"
        asset_class = request.query_params.get('assetclass', None)
        if asset_class is not None:
            funds = Fund.objects.filter(asset_class_id=asset_class)
                    
        # countries // query string = "/funds?country=<country id>"
        country = request.query_params.get('country', None)
        if country is not None:
            funds = Fund.objects.filter(country_id=country)
            
        # industries // query string = "/funds?industry=<industry id>"
        industry = request.query_params.get('industry', None)
        if industry is not None:
            funds = Fund.objects.filter(industry_id=industry)
            
        # issuers // query string = "/funds?issuer=<issuer id>"
        issuer = request.query_params.get('issuer', None)
        if issuer is not None:
            funds = Fund.objects.filter(issuer_id=issuer)
            
        # esg_concerns // query string = "/funds?esg=<esg_concern id>,<esg_concern id>,<esg_concern id>"
            # Returns all funds with a matching esg_concern
        esg = request.query_params.get('esg', None)
        if esg is not None:
            esg = self.request.GET.get("esg", "")
            esg_values = esg.split(",")
            funds = Fund.objects.filter(esg_concern__in=esg_values)
            
        # search for a fund // query string = "/funds?name=<string>"
        #   Returns funds who's name begins with search text
        search_text_name = self.request.query_params.get('name', None)
        if search_text_name is not None:
                funds = Fund.objects.filter(
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
    @action(methods=['post'], detail=True)
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
    
    @action(methods=['get'], detail=False)
    def watchlist(self, request):
        """Handles requests for a users watch list"""
        
        try:
            funds = Fund.objects.filter(watchedsecurity__user_id=request.auth.user.id)
            serializer = FundSerializer(funds, many=True)
            return Response(serializer.data)
        except (Fund.DoesNotExist) as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    @action(methods=['get'], detail=False)
    def reclist(self, request):
        """Handles requests for the current user's recommendation list"""
        
        recs = Recommendation.objects.filter(recommendee=request.auth.user)
        serializer = RecommendationSerializer(recs, many=True)
        return Response(serializer.data)
    
        # HELP: How can I solve for the case where a user is trying to recommend a fund to a user they have already recommended that fund to?
    @action(methods=['post', 'delete'], detail=True)
    def recommend(self, request, pk):
        """Add or remove a recommendation for a fund to another user
        
        - The request must specify which fund (PK), target an existing user (username), and carry a string (note)
        """
        
        try:
            fund = Fund.objects.get(pk=pk)
            recommendee = User.objects.get(username=request.data['username'])
            
            if request.method == "POST":
                recommendation = Recommendation.objects.create(
                    note=request.data['note'],
                    fund=fund,
                    recommender=request.auth.user,
                    recommendee=recommendee
                )
                
            if request.method == "DELETE":
                recommendation = Recommendation.objects.get(
                    fund=fund,
                    recommender=request.auth.user,
                    recommendee=recommendee
                )
                recommendation.delete()
                
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except (Fund.DoesNotExist, User.DoesNotExist) as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)