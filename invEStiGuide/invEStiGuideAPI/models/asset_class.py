from django.db import models
from django.forms import CharField

class AssetClass(models.Model):
   
   asset_class = models.CharField(max_length=200)
   
    # FIXEDINCOME = 'FI'
    # EQUITY = 'EQ'
    # ASSET_CHOICES = [
    #     (FIXEDINCOME, 'Fixed Income'),
    #     (EQUITY, 'Equity'),
    # ]
    # asset = models.CharField(
    #     max_length=2,
    #     choices=ASSET_CHOICES,
    #     default=EQUITY)