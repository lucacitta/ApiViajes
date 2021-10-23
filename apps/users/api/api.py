from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserApiSerializer

from apps.users.models import User

@api_view(['GET',])
def user_api_view(request):
    users = User.objects.all()
    users_serializer = UserApiSerializer(users, many = True)
    return Response(users_serializer.data, status=status.HTTP_200_OK)


@api_view(['GET',])
def user_api_detail_view(request, pk=None):
    users = User.objects.all().filter(id=pk).first()
    users_serializer = UserApiSerializer(users)
    return Response(users_serializer.data, status=status.HTTP_200_OK)