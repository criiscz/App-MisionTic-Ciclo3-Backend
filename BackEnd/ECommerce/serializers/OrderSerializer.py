from rest_framework import serializers
from django.core import serializers as s

from .sellSerializers import SellSerializer
from ..models import Order, User, Sell


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'client', 'order_status', 'date_order']

    def create(self, validated_data):
        initial_data = self.initial_data  # initial_data is all data from request
        order_instance = Order.objects.create(client_id=initial_data['client'], **validated_data)
        sells = initial_data.pop('sells')
        self.create_sells(sells, order_instance)
        return order_instance

    def to_representation(self, instance):
        print("Instance", instance)
        order = Order.objects.get(id=instance[0].id)
        client = User.objects.get(id=order.client_id)
        sells = Sell.objects.filter(order_id=order.id)
        json_data = self.get_json(client, order)
        for i in sells:
            json_data['sells'].append(SellSerializer(i).data)
        return json_data

    def get_json(self, client, order):
        json_data = {
            'id': order.id,
            'date_order': order.date_order,
            'order_status': order.order_status,
            'client': {
                'id': client.id,
                'name': client.name,
                'surname': client.surname
            },
            'sells': []
        }
        return json_data

    def create_sells(self, sells, order_instance):
        for sell in sells:
            Sell.objects.create(order_id=order_instance.id, **sell)
