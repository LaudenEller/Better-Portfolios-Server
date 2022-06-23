from rest_framework import serializers
from invEStiGuideAPI.models.country import Country

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'country', )