from django.db import models
from django.contrib.auth.models import User

class Favorite(models.Model):
    
    issuer = models.ForeignKey("Issuer", related_name="favorite", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="favorite", on_delete=models.CASCADE)