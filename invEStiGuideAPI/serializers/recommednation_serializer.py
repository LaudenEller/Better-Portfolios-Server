from rest_framework import serializers
from invEStiGuideAPI.models.recommendation import Recommendation

class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = (
            'id', 'recommendee', 'recommender', 'note'
        )