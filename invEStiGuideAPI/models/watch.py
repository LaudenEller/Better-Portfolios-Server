from django.db import models
from invEStiGuideAPI.models.fund import Fund
from django.contrib.auth.models import User

class WatchedSecurity(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fund = models.ForeignKey(Fund, on_delete=models.CASCADE)