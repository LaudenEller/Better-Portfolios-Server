from rest_framework import serializers
from invEStiGuideAPI.models.asset_class import Asset_Class

class AssetClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset_Class
        fields = ('id', 'aclass', )