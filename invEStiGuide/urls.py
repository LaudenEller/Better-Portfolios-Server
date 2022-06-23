"""invEStiGuide URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_invEStiGuide import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from invEStiGuideAPI.views import register_user, login_user
from invEStiGuideAPI.views.assetClass import AssetView
from invEStiGuideAPI.views.country import CountryView
from invEStiGuideAPI.views.fund import FundView
from rest_framework import routers
from django.conf.urls import include
from invEStiGuideAPI.views.industry import IndustryView
from invEStiGuideAPI.views.issuer import IssuerView
from invEStiGuideAPI.views.esgConcern import EsgView
from invEStiGuideAPI.views.user import UserView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'funds', FundView, 'fund') # HELP What is the purpose of the string inside that tuple?, Does it allow the HTTP String to be singular
router.register(r'issuers', IssuerView, 'issuer')
router.register(r'assetclasses', AssetView, 'assetClass')
router.register(r'industries', IndustryView, 'industry')
router.register(r'users', UserView, 'user')
router.register(r'esgconcerns', EsgView, 'esgconcern')
router.register(r'countries', CountryView, 'country')
# router.register(r'watched', WatchedView, 'watched_securities')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    # path('', FundView.as_view({'get': 'list'}), name='home'),
]
