from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet)

# from rest_framework_simplejwt.views import (TokenObtainPairView,
#                                             TokenRefreshView, TokenVerifyView)


# jwt_patterns = [
#     path('jwt/create/', TokenObtainPairView.as_view(),
#          name='token_obtain_pair'),
#     path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
# ]

v1_router = DefaultRouter()
v1_router.register('titles', TitleViewSet)
v1_router.register('genres', GenreViewSet)
v1_router.register('categories', CategoryViewSet)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews')
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    # path('v1/', include(jwt_patterns)),
]
