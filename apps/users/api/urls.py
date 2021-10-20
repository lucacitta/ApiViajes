from django.urls import path

from .api import user_api_view, user_api_detail_view


urlpatterns = [
    path('',user_api_view,name= 'users list'),
    path('<int:pk>/',user_api_detail_view,name= 'user detail'),
]