from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from invEStiGuideAPI.models import Recommendation

class RecView(ViewSet):
    
    def destroy(self, request, pk):
        rec = Recommendation.objects.get(pk=pk)
        rec.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)