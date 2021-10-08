from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import User
from ..serializers.UserSerializer import UserSerializer


class UserView(APIView):

    def get(self, _):
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return Response(user_serializer.data)


class UserDetail(APIView):
    msg_user_not_found = {'message': 'Users not found!'}
    msg_parameter_not_found = {'message': 'Parameters not found!'}

    def get(self, _):
        name = self.request.query_params.get('name')
        if name:
            queryset = User.objects.filter(name=name)
            if len(queryset) == 0:
                return Response(self.msg_user_not_found)
            return Response(UserSerializer(queryset, many=True).data)
        else:
            return Response(self.msg_parameter_not_found)
