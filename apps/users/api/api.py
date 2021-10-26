from rest_framework import generics

from .serializers import UserApiSerializer

from apps.users.models import User
from apps.users.authentication_mixins import Authentication

class UserAPiView(Authentication, generics.ListAPIView):
    serializer_class = UserApiSerializer

    def get_queryset(self):
        return User.objects.filter(is_active=True)

class UserApiViewRetrieve(Authentication, generics.RetrieveAPIView):
    serializer_class = UserApiSerializer

    def get_queryset(self, pk = None):
        return self.get_serializer().Meta.model.objects.filter(is_active = True)


'''
@api_view(['GET',])
def user_api_view(request):
    users = User.objects.all()
    users_serializer = UserApiSerializer(users, many = True)
    return Response(users_serializer.data, status=status.HTTP_200_OK)
'''
'''
@api_view(['GET',])
def user_api_detail_view(request, pk=None):
    users = User.objects.all().filter(id=pk).first()
    users_serializer = UserApiSerializer(users)
    return Response(users_serializer.data, status=status.HTTP_200_OK)
'''