from django.db import models

from invEStiGuideAPI.models.country import Country

class Issuer(models.Model):
    
    name = models.CharField(max_length=200)
    image_url = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)