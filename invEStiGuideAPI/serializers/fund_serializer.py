from rest_framework import serializers
from invEStiGuideAPI.models import Fund

class FundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fund
        fields = (
            'id', 'name', 'aclass', 'industry', 
            'country', 'issuer', 'esg_concern', 'esg_rating', 
            'asset_rating', 'image_url', 'is_index'
            )
        depth = 2