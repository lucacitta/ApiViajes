from rest_framework import urlpatterns
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from apps.destinations.views import DestinationViewSet

router = DefaultRouter()
router.register(r'', DestinationViewSet, basename='destinations')

urlpatterns = router.urls