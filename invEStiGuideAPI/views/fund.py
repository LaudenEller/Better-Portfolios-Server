"""View module for handling requests for funds"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from invEStiGuideAPI.models.fund import Fund
from invEStiGuideAPI.models.watch import WatchedSecurity
from invEStiGuideAPI.serializers.fund_serializer import FundSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import action
from invEStiGuideAPI.serializers.watched_serializer import WatchListSerializer
from django.contrib.auth.models import User

class FundView(ViewSet):
    
# get all funds
    def list(self, request):
        """Handles GET requests for all funds
        
        Returns:
            Response -- JSON serialized list of funds
        """
        funds = Fund.objects.all()
        serializer = FundSerializer(funds, many=True)
        return Response(serializer.data)
# add query parameters for 
    #  asset_classes
    # countries
    # esg_concerns
    # industries
    # issuers
    
# get funds that have titles containing the string the user entered in the search bar

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