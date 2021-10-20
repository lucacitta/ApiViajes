from django.utils.translation import activate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.destinations.models import Destination
from .serializers import DestinationApiSerializer



@api_view(['GET'])
def destination_api_view(request):
    if request.method == 'GET':
        destinations = Destination.objects.all().filter(activate = True)
        destinationsSerializer = DestinationApiSerializer(destinations, many = True)
        return Response(destinationsSerializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'message':'Error, el endpoint solo permite get'}, status=status.HTTP_400_BAD_REQUEST)
