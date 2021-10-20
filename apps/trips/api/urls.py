from django.urls import path

from .api import travel_api_view, travel_api_detail_view


urlpatterns = [
    path('',travel_api_view,name= 'travel list'),
    path('<int:pk>/',travel_api_detail_view,name= 'travel detail'),
]
