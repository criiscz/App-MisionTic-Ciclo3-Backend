from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import User
from ..serializers.AccountSerializer import UserSerializer


class UserView(APIView):

    def get(self, request):
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return Response(user_serializer.data)
