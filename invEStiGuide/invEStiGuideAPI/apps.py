from django.apps import AppConfig

# HELP: Is this where I would configure models to a particular app to a particular database?

class AppApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'invEStiGuideAPI'
