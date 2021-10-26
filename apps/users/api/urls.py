from django.urls import path

from .api import UserAPiView, UserApiViewRetrieve

from apps.users.views import Login, Logout, UserToken


urlpatterns = [
    path('',UserAPiView.as_view(),name= 'users list'),
    path('<int:pk>/',UserApiViewRetrieve.as_view(),name= 'user detail'),
    path('login/',Login.as_view(), name='Login'),
    path('logout/',Logout.as_view(), name='Logout'),
    path('refresh-token/', UserToken.as_view(), name='refresh_token')
]