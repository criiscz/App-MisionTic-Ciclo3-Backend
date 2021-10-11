from rest_framework import generics
from rest_framework import views
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .ValidateToken import validate_token
from ..models import User
from ..serializers.UserSerializer import UserSerializer

msg_user_not_found = {'message': 'Users not found!'}
msg_parameter_not_found = {'message': 'Parameters not found!'}


class UserCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        if 'id' not in request.data:
            return Response({"error": "user id not provided"}, status=401)
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        account = request.data['account']
        token_data = {'username': account['username'],
                      'password': account['password']}

        token_serializer = TokenObtainPairSerializer(data=token_data)
        token_serializer.is_valid(raise_exception=True)
        return Response(token_serializer.validated_data, status=201)


class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        valid_data = validate_token(request)
        user_id = User.objects.filter(account_id=valid_data['user_id'], user_type='Seller').first()
        print(user_id)

        if user_id:
            queryset = User.objects.filter(id=kwargs['id_search'])
            return Response(UserSerializer(queryset).data, status=200)
        else:
            return Response({"detail": "Unauthorized User"}, status=401)


class UserById(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        valid_data = validate_token(request)
        user_id = valid_data['user_id']
        user = User.objects.filter(account_id=user_id)

        id_user = 'id' in request.query_params
        only_user = 'only_user' in request.query_params
        only_account = 'only_account' in request.query_params

        if len(request.query_params) > 0:
            user = user[0]
            if id_user:
                return Response({'id': user.id}, status=200)
            elif only_user:
                return Response(
                    {'id': user.id, 'name': user.name, 'surname': user.surname, 'user_type': user.user_type},
                    status=200)
            elif only_account:
                return Response({'username': user.account.username, 'email': user.account.email}, status=200)
        else:
            return Response(UserSerializer(user).data, status=200)
