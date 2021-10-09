
from rest_framework import serializers

from .ProductSerializer import ProductSerializer
from .OrderSerializer import OrderSerializer
from ..models import Sell, Product,Order

class SellSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    order = OrderSerializer()

    class Meta:
        model = Sell
        fields = '__all__'

    def create(self, validated_data):        
        poduct_data = validated_data.pop('product')
        product_instance = Product.objects.create(**poduct_data)
        order_data = validated_data.pop('order')
        order_instance = Order.objects.create(**order_data)
        sell_instance = Sell.objects.create(product_id=product_instance.id,order_id=order_instance.id, **validated_data)
       
        #sell_instance = Sell.objects.create(order_id=order_instance.id, **validated_data)        
        return sell_instance

    def to_representation(self, instance):
        sell = Sell.objects.get(id=instance[0].id)
        order = Order.objects.get(id=sell.order_id)
        product = Product.objects.get(id=sell.product_id)

        return {
            'id': sell.id,
            'product_quantity': sell.product_quantity,
            'order': {
                'id': order.id,
                'date_order': order.date_order,
                'client': order.client,
                'order_status':order.order_status
            },
            'product': {
                'id': product.id,
                'name': product.name,
                'sell_price': product.sell_price
            }
        }
