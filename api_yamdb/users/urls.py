from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, sign_up, get_token

app_name = 'users'

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', get_token),
    path('v1/auth/signup/', sign_up),
]
