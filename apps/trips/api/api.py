from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from apps.trips.models import Travel, Passanger
from .serializers import TravelApiSerializer, PassangerApiSerializer

@api_view(['GET'])
def travel_api_view(request):
    travel = Travel.objects.all().filter(active = True)
    travel_serializer = TravelApiSerializer(travel, many = True)
    return Response(travel_serializer.data, status = status.HTTP_200_OK )

@api_view(['GET'])
def travel_api_detail_view(request, pk=None):

    #Getting the information of the travel
    travel = Travel.objects.all().filter(active=True, id = pk).first()
    travel_serializer = TravelApiSerializer(travel)

    #Getting the information of passangers for the travel
    passanger = Passanger.objects.all().filter(travel=pk)
    if passanger:
        passanger_serializer = PassangerApiSerializer(passanger, many = True)

    data = [{'travel':travel_serializer.data}, {'passangers':passanger_serializer.data}]
    return Response(data = data , status = status.HTTP_200_OK)


