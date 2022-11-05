from django.core.mail import send_mail
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import *
from .serializers import *


class APIUser(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:
            user = User.objects.get_or_create(
                username=request.data['username'], email=request.data['email'])
            confirmation_code = ConfirmationCode.objects.get_or_create(
                user=user[0])
            send_mail(
                'Код для регистрации:',
                f'{user[0]} используйте следующий код: {confirmation_code[0]}',
                'YAMDB@mail.com',
                [request.data['email']],
                fail_silently=False,
            )
            return Response(request.data, status=status.HTTP_201_CREATED)
        except:
            return Response(
                'Пользователь с данным username или email уже существует',
                status=status.HTTP_400_BAD_REQUEST)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    permission_classes = (permissions.AllowAny,)


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    lookup_field = 'username'


class UserDetail(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return User.objects.filter(username=self.request.user)

    def retrieve(self, request):
        queryset = User.objects.filter(username=request.user['username'])
        serializer = UserSerializer(queryset)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.username = request.data.get('username')
        instance.email = request.data.get('email')
        instance.first_name = request.data.get('first_name')
        instance.last_name = request.data.get('last_name')
        instance.bio = request.data.get('bio')
        instance.save()

        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
