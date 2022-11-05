from django.contrib.auth import authenticate
from rest_framework import exceptions, serializers
from rest_framework_simplejwt.authentication import \
    default_user_authentication_rule
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import AccessToken

from api_yamdb.settings import SIMPLE_JWT

from .models import ConfirmationCode, User
from .utils import generate_access_token


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')


class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'] = serializers.CharField(
            max_length=150
        )
        self.fields['confirmation_code'] = serializers.CharField(
            max_length=6
        )
        self.fields['password'] = serializers.PasswordFields(requared=False)

    def validate(self, attrs):
        # authenticate_kwargs = {
        #     self.username_field: attrs[self.username_field],}

        attrs.update({'password': None})
        # print(authenticate_kwargs)
        print(attrs)
        return super(MyTokenObtainPairSerializer, self).validate(attrs)

        try:
            authenticate_kwargs["request"] = self.context["request"]
        except KeyError:
            pass
        self.user = authenticate(**authenticate_kwargs)

        if not default_user_authentication_rule(self.user):
            raise exceptions.AuthenticationFailed(
                self.error_messages["no_active_account"],
                "no_active_account",
            )

        return {}
    # # @classmethod
    # def get_token(cls, user):
    #     token = super().get_token(user)
    #     print(token)
    #     del token['iat']
    #     print(token)
    #     return token.access_token
    # def validate(self, attrs):
    #     user = User.objects.filter(username=attrs['username'])
    #     print(user[0])
    #     user = User.objects.get(username=attrs['username'])
    #     print(user)

    #     if ConfirmationCode.objects.get(user=user).code != attrs['confirmation_code']:
    #         raise serializers.ValidationError('Неверный код')
    #     access = self.get_token(user)
    #     print(access)
    #     attrs.clear()
    #     print(attrs)
    #     attrs['access'] = str(access)
    #     return attrs

    # def validate(self,attr):
    #     print(attr)

    #     data = super().validate(attr)
    #     token = self.get_token(self.user)
    #     print (token)
    # try:
    #     request = self.context["request"]
    #     print(request)
    # except KeyError:
    #     pass
    # request_data = json.loads(request.body)
    # print(request_data)
