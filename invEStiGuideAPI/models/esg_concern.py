from django.db import models

class ESG_Concern(models.Model):
    
    concern = models.CharField(max_length=200)