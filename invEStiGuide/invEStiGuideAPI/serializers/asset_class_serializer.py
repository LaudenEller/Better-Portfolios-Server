from rest_framework import serializers
from invEStiGuideAPI.models.asset_class import AssetClass

class AssetClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetClass
        fields = ('id', 'asset_class', )