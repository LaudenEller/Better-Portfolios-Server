"""View module for handling requests for issuers"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from invEStiGuideAPI.models.favorite import Favorite
from invEStiGuideAPI.models.fund import Fund
from invEStiGuideAPI.models.issuer import Issuer
from rest_framework.decorators import action
from django.contrib.auth.models import User
from invEStiGuideAPI.serializers.fund_serializer import FundSerializer
from invEStiGuideAPI.serializers.issuer_serializer import IssuerSerializer

class IssuerView(ViewSet):
    
    def retrieve(self, request, pk):
        """Get an issuer"""
        
        try:
            funds = Fund.objects.filter(issuer__id = pk)
            issuer = Issuer.objects.get(pk=pk)
            fundSerializer = FundSerializer(funds, many=True)
            issuer.funds = fundSerializer.data
            serializer = IssuerSerializer(issuer)
            return Response(serializer.data)
        except Issuer.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Issuer.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Get all issuers"""
        try:
            issuers = Issuer.objects.all()
            serializer = IssuerSerializer(issuers, many=True)
            return Response(serializer.data)
        except Issuer.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    # Get favorite issuers
    @action(methods=['get'], detail=False)
    def favoritelist(self, request):
        """Handles getting a user's list of favorite issuers"""
        
        try:
            issuers = Issuer.objects.filter(favorite__user_id=request.auth.user.id)
            for issuer in issuers:
                funds = Fund.objects.filter(issuer__id = issuer.id)
                fundSerializer = FundSerializer(funds, many=True)
                issuer.funds = fundSerializer.data
            serializer = IssuerSerializer(issuers, many=True)
            return Response(serializer.data)
        except Issuer.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    # Favorite an issuer
    @action(methods=['post', 'delete'], detail=True)
    def favorite(self, request, pk):
        """Handles adding an issuer to the current user's favorites list"""
        
        try:
            issuer = Issuer.objects.get(pk=pk)
            user = request.auth.user
       
            if request.method == "POST":
                favorite = Favorite.objects.create(
                issuer=issuer,
                user=request.auth.user
            )
            if request.method == "DELETE":
                favorite = Favorite.objects.get(user=user, issuer=issuer)
                favorite.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except (Issuer.DoesNotExist, User.DoesNotExist) as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)