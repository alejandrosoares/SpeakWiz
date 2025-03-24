from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

from utils.response import (
    JsonResponseOk,
    JsonResponseBadRequest
)
from .serializers import (
    UserCreateSerializer,
    UserSerializer,
    LoginRequestSerializer,
    LoginResponseSerializer
)
from .utils.constants import BAD_CREDENTIALS


class SignUpView(generics.CreateAPIView):

    permission_classes = []
    serializer_class = UserCreateSerializer

    @extend_schema(
        operation_id="user_signup",
        summary="User Signup",
        description="Register a new user.",
        request=UserCreateSerializer,
        responses={
            201: UserSerializer,
            400: OpenApiExample(
                'Bad request',
                value={'detail': 'Invalid data'},
                response_only=True,
                status_codes=['400']
            )
        },
        auth=[]  # No authentication required
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    

class LoginView(generics.GenericAPIView):

    permission_classes = []

    @extend_schema(
        operation_id="user_login",
        summary="User Login",
        description="Authenticate a user with email and password.",
        request=LoginRequestSerializer,
        responses={
            200: LoginResponseSerializer,
            400: OpenApiExample(
                'Bad credentials',
                value={'detail': 'Invalid credentials'},
                response_only=True,
                status_codes=['400']
            )
        },
        auth=[]
    )
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=email, password=password)
        if user:
            data = LoginResponseSerializer(user)
            return JsonResponseOk(data.data)
        return JsonResponseBadRequest(BAD_CREDENTIALS)


class UserProfileView(generics.GenericAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="user_profile",
        summary="User Profile",
        description="Retrieve information about the authenticated user.",
        responses={
            200: UserSerializer,
        },
        parameters=[
        OpenApiParameter(
            name='Authorization',
            location=OpenApiParameter.HEADER,
            description='Token-based authentication with the format: Token <token>',
            required=True,
            type=OpenApiTypes.STR,
            default='Token <token>'
        )
    ]
    )
    def get(self, request):
        data = UserSerializer(request.user)
        return JsonResponseOk(data.data)
