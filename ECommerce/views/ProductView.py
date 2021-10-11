from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .ValidateToken import validate_token
from ..models import Product
from ..serializers.ProductSerializer import ProductSerializer


class CreateProductView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        validate_token(request)
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Producto Creado"}, status=201)


class SearchByNameProductView(generics.ListAPIView):
    serializer_class = ProductSerializer,
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        validate_token(request)
        name = self.request.query_params.get('name')
        if name:
            queryset = Product.objects.filter(name__icontains=name)
            if len(queryset) == 0:
                return Response([], status=404)
            return Response(ProductSerializer(queryset, many=True).data)
        return Response(ProductSerializer(Product.objects.all(), many=True).data, status=200)


class SearchByIdProductView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        validate_token(request)
        print(kwargs)
        if len(kwargs) > 0 and kwargs['product_id']:
            queryset = Product.objects.filter(id=kwargs['product_id'])
            if len(queryset) == 0:
                return Response({"message": "Product not found"}, status=404)
            return Response(ProductSerializer(queryset, many=True).data, status=200)
        return Response(ProductSerializer(Product.objects.all(), many=True).data, status=200)
