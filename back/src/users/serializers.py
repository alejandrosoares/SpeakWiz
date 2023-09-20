from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import User


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('name', 'email', 'password')
        extra_fields = {'password': {'write_only': True}}

    def create(self, validated_data):
        name = validated_data.get('name')
        email = validated_data.get('email')
        raw_password = validated_data.get('password')
        new_user = User(name=name, email=email)
        new_user.set_password(raw_password)
        new_user.save()
        new_user.password = '****'
        return new_user


class UserSerializer(serializers.ModelSerializer):

    initialName = serializers.CharField(source='initial_name')
    joined = serializers.DateTimeField(source='date_joined')

    class Meta:
        model = User
        fields = ('id', 'name', 'initialName', 'email', 'joined')


class UserLoginSerializer(UserSerializer):

    token = serializers.SerializerMethodField('get_auth_token')

    class Meta:
        model = User
        fields = ('id', 'name', 'initialName', 'email', 'joined', 'token')

    def get_auth_token(self, user) -> str:
        token, _ = Token.objects.get_or_create(user=user)
        return token.key
