from rest_framework import serializers
from invEStiGuideAPI.models.favorite import Favorite

class CreateFavoriteSerializer(serializers.Serializer):
    
    class Meta:
        model: Favorite
        fields = ('id', 'issuer', 'user')