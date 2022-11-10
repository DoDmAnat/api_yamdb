from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import User


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=254, required=True)
    username = serializers.CharField(max_length=150, required=True)

    def validate_data(self, data):
        if (User.objects.filter(email_iexact=data).exists() or
                User.objects.filter(username_iexact=data).exists):
            raise ValidationError(
                'Пользователь с данным email уже существует.')
        return data

    def validate(self, data):
        if data == 'me':
            raise ValidationError('Недопустимый логин')
        return data

    class Meta:
        fields = ('username', 'email')


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, required=True)
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        fields = ('username', 'confirmation_code')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )


class MeSerializer(serializers.ModelSerializer):
    role = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )
