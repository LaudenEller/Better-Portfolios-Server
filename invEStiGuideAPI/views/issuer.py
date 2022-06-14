"""View module for handling requests for issuers"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from invEStiGuideAPI.models.favorite import Favorite
from invEStiGuideAPI.serializers.favorite_serializer import CreateFavoriteSerializer
from invEStiGuideAPI.models.issuer import Issuer
from rest_framework.decorators import action
from django.contrib.auth.models import User

# HELP: Maybe I don't need a GET method for issuer because the only page 
#   that uses it already has access through the List method for Funds...?
# Get an issuer

class IssuerView(ViewSet):
    
# Favorite an issuer
    @action(methods=['post'], detail=True)
    def favorite(self, request, pk):
        """Handles adding an issuer to the current user's favorites list"""
        
        issuer = Issuer.objects.get(pk=pk)
        favorite = Favorite.objects.create(
            issuer=issuer,
            user=request.auth.user
        ) # HELP: How come this action cannot get triggered by postman?
        serializer = CreateFavoriteSerializer(favorite)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
# Unfavorite an issuer
    @action(methods=['DELETE'], detail=True)
    def unfavorite(self, request, pk):
        """Handles removing an issuer from the current user's favorites list"""
        
        issuer = Issuer.objects.get(pk=pk)
        user = User.objects.get(pk=request.auth.user.id)
        favorite = Favorite.objects.get(user=user, issuer=issuer)
        favorite.delete()
        return Response({'message': 'Favorite removed'}, status=status.HTTP_204_NO_CONTENT)