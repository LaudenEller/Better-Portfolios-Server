from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from invEStiGuideAPI.models.country import Country
from invEStiGuideAPI.serializers.country_serializer import CountrySerializer

class CountryView(ViewSet):
    
    def list(self, request):
        """Get all asset_classs"""
        try:
            assetClasses = Country.objects.all()
            serializer = CountrySerializer(assetClasses, many=True)
            return Response(serializer.data)
        except Country.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)