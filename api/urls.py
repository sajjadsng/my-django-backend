from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, login_view, logout_view

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('users/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='user-detail'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
] 