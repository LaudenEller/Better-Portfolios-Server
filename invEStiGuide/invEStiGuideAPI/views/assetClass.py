from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from invEStiGuideAPI.models.asset_class import AssetClass
from invEStiGuideAPI.serializers.asset_class_serializer import AssetClassSerializer

class AssetView(ViewSet):
    
    def list(self, request):
        """Get all asset_classs"""
        try:
            assetClasses = AssetClass.objects.all()
            serializer = AssetClassSerializer(assetClasses, many=True)
            return Response(serializer.data)
        except AssetClass.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)