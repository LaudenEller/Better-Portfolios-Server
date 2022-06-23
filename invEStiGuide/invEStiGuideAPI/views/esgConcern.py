from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from invEStiGuideAPI.models.esg_concern import ESG_Concern
from invEStiGuideAPI.serializers.esg_serializer import EsgSerializer

class EsgView(ViewSet):
    
    def list(self, request):
        """Get all asset_classs"""
        try:
            assetClasses = ESG_Concern.objects.all()
            serializer = EsgSerializer(assetClasses, many=True)
            return Response(serializer.data)
        except ESG_Concern.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)