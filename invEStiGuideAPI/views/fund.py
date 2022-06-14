"""View module for handling requests for funds"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from invEStiGuideAPI.models.fund import Fund
from invEStiGuideAPI.serializers.fund_serializer import FundSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status

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
