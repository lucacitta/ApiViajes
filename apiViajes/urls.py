from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trips/',include('apps.trips.api.urls')),
    path('destinations/',include('apps.destinations.api.urls')),
    path('users/', include('apps.users.api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
