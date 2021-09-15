__author__ = "Arana Fireheart"

from django.urls import path
from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home')
]