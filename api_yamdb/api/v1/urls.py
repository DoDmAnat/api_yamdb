from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, get_token, sign_up

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet)

auth_patterns = [
    path('token/', get_token),
    path('signup/', sign_up),
]

v1_router = DefaultRouter()
v1_router.register('users', UserViewSet, basename='users')
v1_router.register('titles', TitleViewSet, basename='titles')
v1_router.register('genres', GenreViewSet, basename='genres')
v1_router.register('categories', CategoryViewSet, basename='categories')
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews')
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments')

urlpatterns = [
    path('', include(v1_router.urls)),
    path('auth/', include(auth_patterns)),
]
