from django.conf import settings
from rest_framework import generics
from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from ..models import User
from ..serializers.UserSerializer import UserSerializer

msg_user_not_found = {'message': 'Users not found!'}
msg_parameter_not_found = {'message': 'Parameters not found!'}


class UserCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        print(request)
        print(request.data)
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
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = token_backend.decode(token, verify=False)
        print(kwargs)

        if valid_data['user_id'] != kwargs['pk']:
            string_response = {'detail': 'Unauthorized Request'}
            return Response(string_response, status=401)
        queryset = self.queryset.filter(id=kwargs['id_search'])
        print(queryset)
        return Response(UserSerializer(queryset).data, status=200)
        # return super().get(request, *args, **kwargs)

        # users = User.objects.all()
        # user_serializer = UserSerializer(users, many=True)
        # return Response(user_serializer.data)


# class UserByNameView(APIView):
#     def get(self, _):
#         name = self.request.query_params.get('name')
#         if name:
#             queryset = User.objects.filter(name=name)
#             if len(queryset) == 0:
#                 return Response(msg_user_not_found)
#             return Response(UserSerializer(queryset, many=True).data)
#         else:
#             return Response(msg_parameter_not_found)
#
#
# class UserById(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)
