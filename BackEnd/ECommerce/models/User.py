from django.db import models
from django.utils import timezone

from ..models.Account import Account


class User(models.Model):
    user_types = [
        ('Client', 'client'),
        ('Seller', 'seller'),
        ('Admin', 'admin'),
        ('Operator', 'operator'),
        ('Manager', 'manager'),
        ('Director', 'director')
    ]
    id = models.IntegerField('Id', primary_key=True, default=None)
    name = models.CharField('Name', max_length=30)
    surname = models.CharField('Surname', max_length=30)
    hire_date = models.DateField('Date', default=timezone.now, null=True)
    user_type = models.CharField('User Type', choices=user_types, max_length=30, default='Client')
    account = models.ForeignKey(Account, related_name='account', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f' id:{self.id} : name: {self.name}, account: {self.account}  '

