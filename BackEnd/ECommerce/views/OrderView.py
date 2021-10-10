from rest_framework import generics, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .ValidateToken import validate_token
from ..models import Order, User
from ..serializers.OrderSerializer import OrderSerializer


class CreateOrderView(views.APIView):

    def post(self, request, *args, **kwargs):
        print(request.data)
        valide_data = validate_token(request)
        user_id = User.objects.get(account_id=valide_data['user_id']).id
        if 'client' in request.data:
            serializer = OrderSerializer(data=request.data)
        else:
            serializer = OrderSerializer(data=request.data, client_id=user_id)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Pedido Creado"}, status=201)


class DetailOrderView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        validate_token(request)
        queryset = Order.objects.filter(id=kwargs['pk']).first()
        return Response(self.get_serializer(queryset).data, status=200)


class UpdateOrderView(generics.UpdateAPIView):
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        validate_token(request)
        return super().update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        validated_data = validate_token(request)
        user_id = User.objects.get(account_id=validated_data['user_id']).id
        serializer = self.get_serializer(client_id=user_id, instance=self.get_serializer(kwargs['pk']),
                                         data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=200)

    def patch(self, request, *args, **kwargs):
        validate_token(request)
        order = Order.objects.get(id=kwargs['pk'])
        serializer = OrderSerializer(instance=order, data=request.data,
                                     partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200, data=serializer.data)
        return Response(status=400, data="wrong parameters")
