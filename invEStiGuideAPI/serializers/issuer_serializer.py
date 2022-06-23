from rest_framework import serializers
from invEStiGuideAPI.models.issuer import Issuer

class IssuerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issuer
        fields = (
            'id', 'name', 'image_url', 'country', 'funds'
            )
        depth = 2
