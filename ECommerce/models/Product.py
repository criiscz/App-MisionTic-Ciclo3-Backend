from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('name', max_length=30)
    sell_price = models.FloatField('sell_price')
    buy_price = models.FloatField('buy_price')
