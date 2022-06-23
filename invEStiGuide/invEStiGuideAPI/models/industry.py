from django.db import models

class Industry(models.Model):
    
    industry = models.CharField(max_length=200)