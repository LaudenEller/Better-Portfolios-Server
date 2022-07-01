from django.db import models
from django.forms import CharField

class Asset_Class(models.Model):
   
   asset_class = models.CharField(max_length=200)