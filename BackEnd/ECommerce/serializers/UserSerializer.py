from rest_framework import serializers

from ..models import User, Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        user = User.objects.get(id=instance.id)
        account = Account.objects.get(id=instance.account.id)
        return {
            'id': user.id,
            'name': user.name,
            'surname': user.surname,
            'hire_date': user.hire_date,
            'user_type': user.user_type,
            'account': {
                'id_a': account.id,
                'username': account.username,
                'email': account.email
            }
        }
