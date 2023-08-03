from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewset import UserViewSet, PostViewSet, CommentViewSet, FollowViewSet, LikeViewSet

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'follows', FollowViewSet, basename='follow')
router.register(r'likes', LikeViewSet, basename='like')

# The API URLs are determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]
