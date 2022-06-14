"""View module for handling requests for favorites"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

class FavoriteView(ViewSet):
# create favorite
    def create(self, request):
        """Handles POST requests
        
        Returns:
            Response -- newly created JSON serialized Favorite object and a message
        """
        
        request.data['recommender'] = request.auth.user
        serializer = CreateFavoriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# get all my favorites

# delete favorite