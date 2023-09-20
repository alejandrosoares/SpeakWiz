from django.middleware.csrf import get_token
from django.http.response import JsonResponse
from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.views import APIView

from utils.response import (
    JsonResponseOk,
    JsonResponseBadRequest
)
from .serializers import (
    UserCreateSerializer,
    UserSerializer,
    UserLoginSerializer
)
from .utils.constants import BAD_CREDENTIALS


def get_csrf_token_view(request):
    data = {
        'value': get_token(request)
    }
    return JsonResponse(data)


class SignUpView(generics.CreateAPIView):

    permission_classes = []
    serializer_class = UserCreateSerializer


class LoginView(APIView):

    permission_classes = []

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=email, password=password)
        if user:
            data = UserLoginSerializer(user)
            return JsonResponseOk(data.data)
        return JsonResponseBadRequest(BAD_CREDENTIALS)


class UserInformationView(APIView):

    def get(self, request):
        data = UserSerializer(request.user)
        return JsonResponseOk(data.data)
