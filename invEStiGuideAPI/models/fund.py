from django.db import models
from invEStiGuideAPI.models.esg_concern import ESG_Concern
from invEStiGuideAPI.models.industry import Industry
from invEStiGuideAPI.models.country import Country
from invEStiGuideAPI.models.issuer import Issuer
from invEStiGuideAPI.models.asset_class import AssetClass

class Fund(models.Model):
    
    name = models.CharField(max_length=200)
    asset_class = models.ForeignKey(AssetClass, on_delete=models.CASCADE)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    issuer = models.ForeignKey(Issuer, on_delete=models.CASCADE)
    esg_concern = models.ManyToManyField("ESG_Concern", related_name="fund")
    esg_rating = models.IntegerField()
    asset_rating = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    is_index = models.BooleanField()