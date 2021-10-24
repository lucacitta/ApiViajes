from datetime import timedelta

from django.utils import timezone

from rest_framework.authentication import TokenAuthentication

from apiViajes.settings import base

class ExpiringTokenAuthentication(TokenAuthentication):

    def expires_in(self, token):
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(seconds=base.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return left_time

    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(seconds=0)

    def token_expire_handler(self, token):
        is_expired = self.is_token_expired(token)
        if is_expired:
            print('TOKEN EXPIRADO')
        return is_expired

    def authenticate_credentials(self, key):
        user, token, message = None, None, None
        try:
            token = self.get_model().objects.select_related('user').get(key = key)
            user = token.user
        except self.get_model().DoesNotExist:
            message = 'Token invalido'

        if token is not None:
            if not user.is_active:
                if message is None:
                    message = 'Usuario inactivo o eliminado '

            is_expired = self.token_expire_handler(token)
            if is_expired:
                if message is None:
                    message = 'Su token a expirado'
                else:
                    message += 'ademas su token a expirado'

        return(user, token, message)