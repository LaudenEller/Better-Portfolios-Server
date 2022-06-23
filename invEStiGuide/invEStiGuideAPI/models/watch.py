from django.db import models
from invEStiGuideAPI.models.fund import Fund
from django.contrib.auth.models import User

# HELP: Is there a more djangoesque way of setting up this relationship? If I want to set up many-to-many relationship on the user, should I do a user-extension?
    # ANSW: No, because I will be setting up an external API at some point, it seems prudent to keep the bridge-table models since Django doesn't like cross-database relationships
class WatchedSecurity(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fund = models.ForeignKey(Fund, on_delete=models.CASCADE)