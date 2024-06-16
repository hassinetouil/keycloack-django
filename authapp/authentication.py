from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from keycloak import KeycloakOpenID
from django.conf import settings
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)

class KeycloakAuthentication(BaseAuthentication):
    def authenticate(self, request):
        import pdb
        pdb.set_trace()
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None
        try:
            token = auth_header.split(' ')[1]
            logger.info(f"Token: {token}")
            keycloak_openid = KeycloakOpenID(server_url=settings.KEYCLOAK_SERVER_URL,
                                             client_id=settings.KEYCLOAK_CLIENT_ID,
                                             realm_name=settings.KEYCLOAK_REALM_NAME,
                                             client_secret_key=settings.KEYCLOAK_CLIENT_SECRET)
            config_well_known = keycloak_openid.well_known()
            token1 = keycloak_openid.token("hassine", "test")
            keycloak_openid.userinfo(token1['access_token'])
            user_info = keycloak_openid.userinfo(token)
            if 'preferred_username' in user_info:
                username = user_info['preferred_username']
                user, _ = User.objects.get_or_create(username=username)
                return user, token
        except Exception:
            raise AuthenticationFailed('Invalid token')
        return None
