from datetime import datetime
from django.contrib.sessions.models import Session

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import status

from .authentication_mixins import Authentication
from .api.serializers import UserLoginSerializer


class UserToken(APIView):
    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')
        try:
            user_token = Token.objects.get(
                user = UserLoginSerializer().Meta.model.objects.filter(username = username).first()
            )
            return Response({'token':user_token.key})
        except:
            return Response({
                'error':'Credenciales enviadas incorrectas'
            }, status=status.HTTP_400_BAD_REQUEST)

class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context={'request':request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token,created = Token.objects.get_or_create(user=user)
                user_serializer = UserLoginSerializer(user)
                if created:
                    return Response({
                        'token':token.key,
                        'user':user_serializer.data,
                        'message':'Inicio de sesion exitoso'
                    }, status = status.HTTP_201_CREATED)
                else:
                    '''
                    Estamos tomando que cuando se intenta ingresar dos veces, se cierren las sesiones activas.
                    Luego borra el token viejo y genera el nuevo, de esta manera te deja ingresar igualmente.
                    Tambien se podria prohibir el ingreso si esto sucede.
                    '''
                    all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                    token.delete()
                    token = Token.objects.create(user=user)
                    return Response({
                        'token':token.key,
                        'user':user_serializer.data,
                        'message':'Inicio de sesion exitoso'
                    }, status = status.HTTP_201_CREATED)
            else:
                return Response({'error':'El usuario no se encuentra habilitado para iniciar sesion'},
                                    status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error':'Credenciales incorrectas'}, status=status.HTTP_400_BAD_REQUEST)

class Logout(APIView):

    def post(self, request, *args, **kwargs):
        token = request.POST.get('token')
        token = Token.objects.filter(key = token).first()
        if token != None:
            if token:
                user = token.user
                all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                token.delete()
                session_message = 'Sesiones de usuario eliminadas'
                token_message = 'Token eliminado'
                return Response({'token_message':token_message, 'session_message':session_message},
                                    status=status.HTTP_200_OK)
            return Response({'error':'No se a encontrado usuario con esas credenciales'},
                                    status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error':'No se encontro el token'},status=status.HTTP_400_BAD_REQUEST)
