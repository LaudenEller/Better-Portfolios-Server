from django.db import models
from django.forms import CharField

class Asset_Class(models.Model):
   
   aclass = models.CharField(max_length=200)