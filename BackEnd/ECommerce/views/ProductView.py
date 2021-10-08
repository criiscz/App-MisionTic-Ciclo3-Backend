from django.conf import settings
from django.views import View
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend

from ..models import Product
from ..serializers.ProductSerializer import ProductSerializer
from ..serializers.UserSerializer import UserSerializer


class AllProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = token_backend.decode(token, verify=False)
        print(kwargs)
        print(valid_data)
        print(self.queryset[0])

        # if valid_data['user_id'] != kwargs['pk']:
        #     string_response = {'detail': 'Unauthorized Request'}
        #     return Response(string_response, status=401)
        # queryset = self.queryset.filter(id=kwargs['id_search'])
        # print(queryset)
        # return Response(ProductSerializer(self.queryset), status=200)
        return super().get(request, *args, **kwargs)


class CreateProductView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = token_backend.decode(token, verify=False)
        print(request)
        print(valid_data)
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Producto Creado", status=201)
