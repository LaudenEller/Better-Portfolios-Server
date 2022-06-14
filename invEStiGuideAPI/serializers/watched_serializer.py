from rest_framework import serializers
from invEStiGuideAPI.models.watch import WatchedSecurity

class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchedSecurity
        fields = (
            'id', 'fund', 'user'
        )