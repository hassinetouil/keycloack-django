from django.contrib.auth.backends import BaseBackend
from keycloak.keycloak_openid import KeycloakOpenID
from django.conf import settings
from django.contrib.auth.models import User


class KeycloakBackend(BaseBackend):
    def authenticate(self, request, token=None):
        keycloak_openid = KeycloakOpenID(server_url=settings.KEYCLOAK_SERVER_URL,
                                         client_id=settings.KEYCLOAK_CLIENT_ID,
                                         realm_name=settings.KEYCLOAK_REALM_NAME,
                                         client_secret_key=settings.KEYCLOAK_CLIENT_SECRET)
        try:
            user_info = keycloak_openid.userinfo(token)
            if 'preferred_username' in user_info:
                username = user_info['preferred_username']
                user, _ = User.objects.get_or_create(username=username)
                return user
        except Exception as e:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
