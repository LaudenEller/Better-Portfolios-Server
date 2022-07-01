from django.db import models
from django.forms import CharField

class Asset_Class(models.Model):
   
   AClass = models.CharField(max_length=200)