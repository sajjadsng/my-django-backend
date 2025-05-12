from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import CustomUser
from .serializers import UserSerializer, UserCreateSerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.AllowAny]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer

    @swagger_auto_schema(
        operation_description='ثبت نام کاربر جدید',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['email', 'username', 'password'],
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='ایمیل کاربر'),
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='نام کاربری'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='رمز عبور'),
                'role': openapi.Schema(
                    type=openapi.TYPE_STRING, 
                    description='نقش کاربر (employee یا admin)',
                    enum=['employee', 'admin'],
                    default='employee'
                ),
            },
        ),
        responses={
            201: openapi.Response(
                description='ثبت نام موفق',
                schema=UserSerializer
            ),
            400: 'اطلاعات ناقص یا نامعتبر',
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['email', 'password'],
        properties={
            'email': openapi.Schema(type=openapi.TYPE_STRING, description='ایمیل کاربر'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='رمز عبور'),
        },
    ),
    responses={
        200: openapi.Response(
            description='لاگین موفق',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'access': openapi.Schema(type=openapi.TYPE_STRING, description='توکن دسترسی'),
                    'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='توکن تازه‌سازی'),
                    'user': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                            'email': openapi.Schema(type=openapi.TYPE_STRING),
                            'username': openapi.Schema(type=openapi.TYPE_STRING),
                        }
                    ),
                }
            )
        ),
        400: 'اطلاعات ناقص',
        401: 'اطلاعات نامعتبر',
    }
)
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    if not email or not password:
        return Response(
            {'error': 'Please provide both email and password'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = authenticate(email=email, password=password)
    
    if user is None:
        return Response(
            {'error': 'Invalid credentials'},
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    refresh = RefreshToken.for_user(user)
    
    return Response({
        'access': str(refresh.access_token),
        'refresh': str(refresh),
        'user': {
            'id': user.id,
            'email': user.email,
            'username': user.username
        }
    })

@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['refresh'],
        properties={
            'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='توکن تازه‌سازی'),
        },
    ),
    responses={
        200: openapi.Response(
            description='لاگ‌اوت موفق',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'message': openapi.Schema(type=openapi.TYPE_STRING, description='پیام موفقیت'),
                }
            )
        ),
        400: 'توکن نامعتبر',
        401: 'توکن منقضی شده',
    }
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    try:
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response({'error': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)
            
        # Simply return success message
        return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
