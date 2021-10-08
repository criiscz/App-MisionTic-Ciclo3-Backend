from rest_framework import serializers

from .AccountSerializer import AccountSerializer
from ..models import User, Account


class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer()

    class Meta:
        model = User
        fields = ['id', 'name', 'surname', 'account']

    def create(self, validated_data):
        print(validated_data)
        account_data = validated_data.pop('account')
        account_instance = Account.objects.create(**account_data)
        user_instance = User.objects.create(account_id=account_instance.id ,**validated_data)
        return user_instance

    def to_representation(self, instance):
        user = User.objects.get(id=instance[0].id)
        account = Account.objects.get(id=instance[0].account.id)
        return {
            'id': user.id,
            'name': user.name,
            'surname': user.surname,
            'user_type': user.user_type,
            'account': {
                'username': account.username,
                'email': account.email
            }
        }
