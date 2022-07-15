from django.contrib.auth import login
from knox.auth import TokenAuthentication
from rest_framework import permissions, generics
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from .serializers import UserSerializer
from authentication.models import User
from rest_framework.response import Response


class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = [TokenAuthentication]

    def post(self, request, format = None):
        serializer = AuthTokenSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format = None)        


class RegisterApi(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]        