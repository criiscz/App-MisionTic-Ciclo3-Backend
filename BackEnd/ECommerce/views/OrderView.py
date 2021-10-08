from django.conf import settings
from rest_framework import generics, views
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend

from ..serializers.OrderSerializer import OrderSerializer


class CreateOrderView(views.APIView):

    def post(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = token_backend.decode(token, verify=False)
        id_account = valid_data['id_user']

        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message": "Pedido Creado"}, status=201)
