from rest_framework import serializers
from invEStiGuideAPI.models.esg_concern import ESG_Concern

class EsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ESG_Concern
        fields = ('id', 'concern', )