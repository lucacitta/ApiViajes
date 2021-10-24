from django.urls import path

from .api import user_api_view, user_api_detail_view

from apps.users.views import Login, Logout


urlpatterns = [
    path('',user_api_view,name= 'users list'),
    path('<int:pk>/',user_api_detail_view,name= 'user detail'),
    path('login',Login.as_view(), name='Login'),
    path('logout',Logout.as_view(), name='Logout') 
]