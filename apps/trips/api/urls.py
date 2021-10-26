from django.urls import path

from .api import Travel_api_view, Travel_api_retrieve_view


urlpatterns = [
    path('',Travel_api_view.as_view(), name= 'travel list'),
    path('<int:pk>/',Travel_api_retrieve_view,name= 'travel retrieve'),
]
