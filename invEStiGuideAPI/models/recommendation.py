from django.db import models
from invEStiGuideAPI.models.fund import Fund
from django.contrib.auth.models import User
class Recommendation(models.Model):
    
    recommender = models.ForeignKey(User, related_name='my_rec', on_delete=models.CASCADE)
    recommendee = models.ForeignKey(User, related_name='rec_for_me', on_delete=models.CASCADE)
    fund = models.ForeignKey(Fund, on_delete=models.CASCADE)
    note = models.CharField(max_length=200)
    