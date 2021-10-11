from rest_framework import serializers

from .sellSerializers import SellSerializer
from ..models import Order, User, Sell, Product


class OrderSerializer(serializers.ModelSerializer):

    def __init__(self, instance=None, client_id=None, **kwargs):
        self.client_id = client_id
        super().__init__(instance, **kwargs)

    class Meta:
        model = Order
        fields = ['order_status', 'date_order']

    def create(self, validated_data):
        initial_data = self.initial_data
        if self.client_id is not None:
            order_instance = Order.objects.create(client_id=self.client_id, **validated_data)
        else:
            order_instance = Order.objects.create(client_id=initial_data['client'], **validated_data)
        sells = initial_data.pop('sells')
        self.create_sells(sells, order_instance)
        return order_instance

    def to_representation(self, instance):
        order = Order.objects.get(id=instance.id)
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
            'order_status': order.status_list[int(order.order_status)][1],
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
            product = Product.objects.get(id=sell['product'])
            Sell.objects.create(order_id=order_instance.id, product_id=product.id,
                                product_quantity=sell['product_quantity'])
