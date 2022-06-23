from rest_framework import serializers
from invEStiGuideAPI.models.industry import Industry

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ('id', 'industry', )