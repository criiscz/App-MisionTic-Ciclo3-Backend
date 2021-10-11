from django.db import models
from django.db.models import BigAutoField

from .User import User


class Order(models.Model):
    status_list = [
        (0, 'En Espera'),
        (1, 'En Preparación'),
        (2, 'En Ruta'),
        (3, 'Entregado'),
        (4, 'Cancelado')
    ]

    id = BigAutoField('Id', primary_key=True)

    date_order = models.DateTimeField('Date Order', auto_now_add=True)
    client = models.ForeignKey(User, related_name='client', on_delete=models.CASCADE)
    seller = models.ForeignKey(User, related_name='seller', on_delete=models.CASCADE, null=True)
    order_status = models.CharField('Order Status', max_length=20, choices=status_list, default=0)

    def __str__(self):
        return f'id: {self.id}%n order status {self.order_status}:'