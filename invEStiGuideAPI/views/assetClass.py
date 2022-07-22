from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from invEStiGuideAPI.models.asset_class import Asset_Class
from invEStiGuideAPI.serializers.asset_class_serializer import AssetClassSerializer

class AssetView(ViewSet):
    
    def list(self, request):
        """Get all asset_classs"""
        try:
            assetClasses = Asset_Class.objects.all()
            serializer = AssetClassSerializer(assetClasses, many=True)
            return Response(serializer.data)
        except Asset_Class.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)