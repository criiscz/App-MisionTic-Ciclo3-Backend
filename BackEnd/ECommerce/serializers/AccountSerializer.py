from rest_framework import serializers

from ..models import Account


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['username', 'password', 'email']

    def to_representation(self, instance):
        account = Account.objects.get(id=instance.id)
        return {
            'username': account.name,
            'email': account.email
        }
