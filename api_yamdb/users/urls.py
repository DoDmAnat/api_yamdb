from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import *

app_name = 'users'

router = DefaultRouter()
# router.register('auth/signup', SignupViewSet, basename='auth/signup')
router.register('users', UsersViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', MyTokenObtainPairView.as_view()),
    path('v1/auth/signup/', APIUser.as_view()),
    path('v1/users/me', UserDetail.as_view())
]
