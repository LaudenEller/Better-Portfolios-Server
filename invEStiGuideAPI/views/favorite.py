"""View module for handling requests for favorites"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from invEStiGuideAPI.models.favorite import Favorite

class FavoriteView(ViewSet):

# get all my favorites