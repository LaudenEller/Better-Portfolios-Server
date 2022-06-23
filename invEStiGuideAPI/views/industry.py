from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from invEStiGuideAPI.models.industry import Industry
from invEStiGuideAPI.serializers.industry_serializer import IndustrySerializer

class IndustryView(ViewSet):
    
    def list(self, request):
        """Get all industries"""
        try:
            industries = Industry.objects.all()
            serializer = IndustrySerializer(industries, many=True)
            return Response(serializer.data)
        except Industry.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)