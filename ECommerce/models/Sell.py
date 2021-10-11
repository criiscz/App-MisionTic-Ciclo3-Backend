from django.db import models

from . import Order
from .Product import Product


class Sell(models.Model):
    id = models.BigAutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    product_quantity = models.IntegerField('Product quantity', default=0)
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)