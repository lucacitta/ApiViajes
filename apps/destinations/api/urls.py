from django.urls import path

from .api import destination_api_view


urlpatterns = [
    path('',destination_api_view, name= 'destination list'),
]
