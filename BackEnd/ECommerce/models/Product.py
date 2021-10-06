from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=30)
    sell_price = models.FloatField('Sell price')
    buy_price = models.FloatField('Buy price')
