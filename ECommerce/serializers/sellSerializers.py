from rest_framework import serializers

from .ProductSerializer import ProductSerializer
from ..models import Sell, Product


class SellSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Sell
        fields = '__all__'

    def create(self, validated_data):
        product = validated_data.pop('product')
        product_instance = Product.objects.create(**product)
        sell_instance = Sell.objects.create(product_id=product_instance.id, **validated_data)

        return sell_instance

    def to_representation(self, instance):
        sell = Sell.objects.get(id=instance.id)
        product = Product.objects.get(id=sell.product_id)

        return {
            'id': sell.id,
            'product_quantity': sell.product_quantity,
            'product': {
                'id': product.id,
                'name': product.name,
                'sell_price': product.sell_price
            }
        }
