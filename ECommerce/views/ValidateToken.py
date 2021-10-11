from django.conf import settings
from rest_framework_simplejwt.backends import TokenBackend


def validate_token(request):
    token = request.META.get('HTTP_AUTHORIZATION')[7:]
    token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
    return token_backend.decode(token, verify=False)