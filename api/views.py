from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import (
    CustomUser, Project, Employee, InvestorProfile, LegalDocument, 
    EmergencyContact, EmployeeDocuments, ProjectStatus, EmploymentType, 
    Gender, Roles
)
from .serializers import (
    UserRegistrationSerializer, UserProfileSerializer, LoginSerializer,
    ProjectSerializer, ProjectCreateSerializer, EmployeeSerializer, 
    EmployeeCreateSerializer, InvestorProfileSerializer, LegalDocumentSerializer,
    ProjectStatusSerializer, EmploymentTypeSerializer, GenderSerializer, RolesSerializer,
    FileUploadSerializer
)
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.conf import settings
from rest_framework.parsers import MultiPartParser, FormParser
import os
from django.core.files.storage import default_storage

User = get_user_model()

# Error Codes
AUTH_ERROR_CODES = {
    'AS1001': 'InvalidRegistrationData',
    'AS1002': 'EmailAlreadyExists',
    'AS1003': 'InvalidLoginCredentials',
    'AS1004': 'UserNotFound',
    'AS1005': 'AuthenticationRequired',
    'AS1006': 'InvalidLogoutToken',
}

PROJECT_ERROR_CODES = {
    'AS2001': 'ProjectNotFound',
    'AS2002': 'InvalidProjectData',
    'AS2003': 'ProjectCreationFailed',
    'AS2004': 'ProjectUpdateFailed',
    'AS2005': 'ProjectDeleteFailed',
}

EMPLOYEE_ERROR_CODES = {
    'AS3001': 'EmployeeNotFound',
    'AS3002': 'InvalidEmployeeData',
    'AS3003': 'EmployeeCreationFailed',
    'AS3004': 'EmployeeUpdateFailed',
    'AS3005': 'EmployeeDeleteFailed',
}

INVESTOR_ERROR_CODES = {
    'AS4001': 'InvestorProfileNotFound',
    'AS4002': 'InvalidInvestorData',
    'AS4003': 'InvestorProfileCreationFailed',
    'AS4004': 'InvestorProfileUpdateFailed',
    'AS4005': 'InvestorProfileDeleteFailed',
}

DOCUMENT_ERROR_CODES = {
    'AS5001': 'LegalDocumentNotFound',
    'AS5002': 'InvalidDocumentData',
    'AS5003': 'DocumentCreationFailed',
    'AS5004': 'DocumentUpdateFailed',
    'AS5005': 'DocumentDeleteFailed',
}

FILE_ERROR_CODES = {
    'AS6001': 'FileUploadFailed',
    'AS6002': 'InvalidFileType',
    'AS6003': 'FileTooLarge',
}

@swagger_auto_schema(
    method='get',
    responses={
        200: openapi.Response(
            description='لیست تمام API ها',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'authentication': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'register': openapi.Schema(type=openapi.TYPE_STRING, description='ثبت‌نام'),
                            'login': openapi.Schema(type=openapi.TYPE_STRING, description='ورود'),
                            'logout': openapi.Schema(type=openapi.TYPE_STRING, description='خروج'),
                            'profile': openapi.Schema(type=openapi.TYPE_STRING, description='پروفایل کاربر'),
                        }
                    ),
                    'projects': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'list': openapi.Schema(type=openapi.TYPE_STRING, description='لیست پروژه‌ها'),
                            'create': openapi.Schema(type=openapi.TYPE_STRING, description='ایجاد پروژه'),
                            'detail': openapi.Schema(type=openapi.TYPE_STRING, description='جزئیات پروژه'),
                        }
                    ),
                    'employees': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'list': openapi.Schema(type=openapi.TYPE_STRING, description='لیست کارمندان'),
                            'create': openapi.Schema(type=openapi.TYPE_STRING, description='ایجاد کارمند'),
                            'detail': openapi.Schema(type=openapi.TYPE_STRING, description='جزئیات کارمند'),
                        }
                    ),
                    'investor_profiles': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'list': openapi.Schema(type=openapi.TYPE_STRING, description='لیست پروفایل‌های سرمایه‌گذار'),
                            'create': openapi.Schema(type=openapi.TYPE_STRING, description='ایجاد پروفایل سرمایه‌گذار'),
                            'detail': openapi.Schema(type=openapi.TYPE_STRING, description='جزئیات پروفایل سرمایه‌گذار'),
                        }
                    ),
                    'legal_documents': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'list': openapi.Schema(type=openapi.TYPE_STRING, description='لیست مدارک قانونی'),
                            'create': openapi.Schema(type=openapi.TYPE_STRING, description='ایجاد مدرک قانونی'),
                            'detail': openapi.Schema(type=openapi.TYPE_STRING, description='جزئیات مدرک قانونی'),
                        }
                    ),
                    'choices': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'project_status': openapi.Schema(type=openapi.TYPE_STRING, description='وضعیت‌های پروژه'),
                            'employment_type': openapi.Schema(type=openapi.TYPE_STRING, description='انواع استخدام'),
                            'gender': openapi.Schema(type=openapi.TYPE_STRING, description='جنسیت‌ها'),
                            'roles': openapi.Schema(type=openapi.TYPE_STRING, description='نقش‌ها'),
                        }
                    ),
                    'upload': openapi.Schema(type=openapi.TYPE_STRING, description='آپلود فایل'),
                }
            )
        )
    }
)
@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request):
    """
    API Root - لیست تمام endpoint های موجود
    """
    return Response({
        'authentication': {
            'register': '/api/register/',
            'login': '/api/login/',
            'logout': '/api/logout/',
            'profile': '/api/profile/',
        },
        'projects': {
            'list': '/api/projects/',
            'create': '/api/projects/',
            'detail': '/api/projects/{id}/',
            'project_employee': '/api/projects/{project_id}/employees/{employee_id}/',
        },
        'employees': {
            'list': '/api/employees/',
            'create': '/api/employees/',
            'detail': '/api/employees/{id}/',
        },
        'investor_profiles': {
            'list': '/api/investor-profiles/',
            'create': '/api/investor-profiles/',
            'detail': '/api/investor-profiles/{id}/',
        },
        'legal_documents': {
            'list': '/api/legal-documents/',
            'create': '/api/legal-documents/',
            'detail': '/api/legal-documents/{id}/',
        },
        'choices': {
            'project_status': '/api/choices/project-status/',
            'employment_type': '/api/choices/employment-type/',
            'gender': '/api/choices/gender/',
            'roles': '/api/choices/roles/',
        },
        'upload': '/api/upload/',
        'swagger': '/swagger/',
        'redoc': '/redoc/',
    })

# Existing Authentication Views
@swagger_auto_schema(
    method='post',
    request_body=UserRegistrationSerializer,
    responses={
        201: openapi.Response(description='Registration Successful', schema=UserProfileSerializer),
        'AS1001': openapi.Response(description='InvalidRegistrationData'),
        'AS1002': openapi.Response(description='EmailAlreadyExists'),
    }
)
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'message': 'ثبت‌نام با موفقیت انجام شد',
            'user': UserProfileSerializer(user).data,
            'tokens': {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }
        }, status=status.HTTP_201_CREATED)
    
    # Check for specific errors
    if 'email' in serializer.errors:
        return Response({
            'error_code': 'AS1002',
            'error_message': AUTH_ERROR_CODES['AS1002']
        }, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({
        'error_code': 'AS1001',
        'error_message': AUTH_ERROR_CODES['AS1001'],
        'details': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='post',
    request_body=LoginSerializer,
    responses={
        200: openapi.Response(
            description='Login Successful',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'message': openapi.Schema(type=openapi.TYPE_STRING),
                    'user': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                            'email': openapi.Schema(type=openapi.TYPE_STRING),
                            'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                            'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                            'mobile': openapi.Schema(type=openapi.TYPE_STRING),
                        }
                    ),
                    'tokens': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'access': openapi.Schema(type=openapi.TYPE_STRING),
                            'refresh': openapi.Schema(type=openapi.TYPE_STRING),
                        }
                    ),
                }
            )
        ),
        'AS1001': openapi.Response(description='InvalidLoginData'),
        'AS1003': openapi.Response(description='InvalidLoginCredentials'),
    }
)
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = authenticate(email=email, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'ورود موفقیت‌آمیز',
                'user': UserProfileSerializer(user).data,
                'tokens': {
                    'access': str(refresh.access_token),
                    'refresh': str(refresh),
                }
            })
        else:
            return Response({
                'error_code': 'AS1003',
                'error_message': AUTH_ERROR_CODES['AS1003']
            }, status=status.HTTP_401_UNAUTHORIZED)
    
    return Response({
        'error_code': 'AS1001',
        'error_message': AUTH_ERROR_CODES['AS1001'],
        'details': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='Refresh Token'),
        }
    ),
    responses={
        200: openapi.Response(
            description='Logout Successful',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'message': openapi.Schema(type=openapi.TYPE_STRING),
                }
            )
        ),
        'AS1005': openapi.Response(description='AuthenticationRequired'),
        'AS1006': openapi.Response(description='InvalidLogoutToken'),
    }
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        refresh_token = request.data.get('refresh')
        if refresh_token:
            token = RefreshToken(refresh_token)
            token.blacklist()
        return Response({'message': 'خروج موفقیت‌آمیز'})
    except Exception as e:
        return Response({
            'error_code': 'AS1006',
            'error_message': AUTH_ERROR_CODES['AS1006']
        }, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='get',
    responses={
        200: openapi.Response(description='User Profile', schema=UserProfileSerializer),
        'AS1005': openapi.Response(description='AuthenticationRequired'),
    }
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    serializer = UserProfileSerializer(request.user)
    return Response(serializer.data)

class UserProfileByIdView(APIView):
    @swagger_auto_schema(
        operation_description="Get User Profile by ID",
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_PATH,
                description='User ID',
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        responses={
            200: UserProfileSerializer,
            'AS1004': openapi.Response(description='UserNotFound'),
            'AS1005': openapi.Response(description='AuthenticationRequired'),
        }
    )
    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({
                'error_code': 'AS1004',
                'error_message': AUTH_ERROR_CODES['AS1004']
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

# New Project Management Views
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProjectCreateSerializer
        return ProjectSerializer
    
    @swagger_auto_schema(
        operation_description="دریافت لیست پروژه‌ها",
        responses={
            200: ProjectSerializer(many=True),
            401: 'احراز هویت نشده'
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="ایجاد پروژه جدید",
        request_body=ProjectCreateSerializer,
        responses={
            201: ProjectSerializer,
            400: 'اطلاعات نامعتبر',
            401: 'احراز هویت نشده'
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        operation_description="دریافت جزئیات پروژه",
        responses={
            200: ProjectSerializer,
            404: 'پروژه یافت نشد',
            401: 'احراز هویت نشده'
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="به‌روزرسانی پروژه",
        request_body=ProjectSerializer,
        responses={
            200: ProjectSerializer,
            400: 'اطلاعات نامعتبر',
            404: 'پروژه یافت نشد',
            401: 'احراز هویت نشده'
        }
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="حذف پروژه",
        responses={
            204: 'پروژه حذف شد',
            404: 'پروژه یافت نشد',
            401: 'احراز هویت نشده'
        }
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return EmployeeCreateSerializer
        return EmployeeSerializer
    
    @swagger_auto_schema(
        operation_description="دریافت لیست کارمندان",
        responses={
            200: EmployeeSerializer(many=True),
            401: 'احراز هویت نشده'
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="ایجاد کارمند جدید",
        request_body=EmployeeCreateSerializer,
        responses={
            201: EmployeeSerializer,
            400: 'اطلاعات نامعتبر',
            401: 'احراز هویت نشده'
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        operation_description="دریافت جزئیات کارمند",
        responses={
            200: EmployeeSerializer,
            404: 'کارمند یافت نشد',
            401: 'احراز هویت نشده'
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="به‌روزرسانی کارمند",
        request_body=EmployeeSerializer,
        responses={
            200: EmployeeSerializer,
            400: 'اطلاعات نامعتبر',
            404: 'کارمند یافت نشد',
            401: 'احراز هویت نشده'
        }
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="حذف کارمند",
        responses={
            204: 'کارمند حذف شد',
            404: 'کارمند یافت نشد',
            401: 'احراز هویت نشده'
        }
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

# Choice Fields Views
@swagger_auto_schema(
    method='get',
    responses={
        200: openapi.Response(
            description='لیست وضعیت‌های پروژه',
            schema=ProjectStatusSerializer(many=True)
        )
    }
)
@api_view(['GET'])
@permission_classes([AllowAny])
def project_status_choices(request):
    choices = [{'value': choice[0], 'label': choice[1]} for choice in ProjectStatus.choices]
    return Response(choices)

@swagger_auto_schema(
    method='get',
    responses={
        200: openapi.Response(
            description='لیست انواع استخدام',
            schema=EmploymentTypeSerializer(many=True)
        )
    }
)
@api_view(['GET'])
@permission_classes([AllowAny])
def employment_type_choices(request):
    choices = [{'value': choice[0], 'label': choice[1]} for choice in EmploymentType.choices]
    return Response(choices)

@swagger_auto_schema(
    method='get',
    responses={
        200: openapi.Response(
            description='لیست جنسیت‌ها',
            schema=GenderSerializer(many=True)
        )
    }
)
@api_view(['GET'])
@permission_classes([AllowAny])
def gender_choices(request):
    choices = [{'value': choice[0], 'label': choice[1]} for choice in Gender.choices]
    return Response(choices)

@swagger_auto_schema(
    method='get',
    responses={
        200: openapi.Response(
            description='لیست نقش‌ها',
            schema=RolesSerializer(many=True)
        )
    }
)
@api_view(['GET'])
@permission_classes([AllowAny])
def roles_choices(request):
    choices = [{'value': choice[0], 'label': choice[1]} for choice in Roles.choices]
    return Response(choices) 

# InvestorProfile Management Views
class InvestorProfileListCreateView(generics.ListCreateAPIView):
    queryset = InvestorProfile.objects.all()
    serializer_class = InvestorProfileSerializer
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        operation_description="دریافت لیست پروفایل‌های سرمایه‌گذار",
        responses={
            200: InvestorProfileSerializer(many=True),
            401: 'احراز هویت نشده'
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="ایجاد پروفایل سرمایه‌گذار جدید",
        request_body=InvestorProfileSerializer,
        responses={
            201: InvestorProfileSerializer,
            400: 'اطلاعات نامعتبر',
            401: 'احراز هویت نشده'
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class InvestorProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvestorProfile.objects.all()
    serializer_class = InvestorProfileSerializer
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        operation_description="دریافت جزئیات پروفایل سرمایه‌گذار",
        responses={
            200: InvestorProfileSerializer,
            404: 'پروفایل یافت نشد',
            401: 'احراز هویت نشده'
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="به‌روزرسانی پروفایل سرمایه‌گذار",
        request_body=InvestorProfileSerializer,
        responses={
            200: InvestorProfileSerializer,
            400: 'اطلاعات نامعتبر',
            404: 'پروفایل یافت نشد',
            401: 'احراز هویت نشده'
        }
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="حذف پروفایل سرمایه‌گذار",
        responses={
            204: 'پروفایل حذف شد',
            404: 'پروفایل یافت نشد',
            401: 'احراز هویت نشده'
        }
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

# LegalDocument Management Views
class LegalDocumentListCreateView(generics.ListCreateAPIView):
    queryset = LegalDocument.objects.all()
    serializer_class = LegalDocumentSerializer
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        operation_description="دریافت لیست مدارک قانونی",
        responses={
            200: LegalDocumentSerializer(many=True),
            401: 'احراز هویت نشده'
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="ایجاد مدرک قانونی جدید",
        request_body=LegalDocumentSerializer,
        responses={
            201: LegalDocumentSerializer,
            400: 'اطلاعات نامعتبر',
            401: 'احراز هویت نشده'
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class LegalDocumentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LegalDocument.objects.all()
    serializer_class = LegalDocumentSerializer
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        operation_description="دریافت جزئیات مدرک قانونی",
        responses={
            200: LegalDocumentSerializer,
            404: 'مدرک یافت نشد',
            401: 'احراز هویت نشده'
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="به‌روزرسانی مدرک قانونی",
        request_body=LegalDocumentSerializer,
        responses={
            200: LegalDocumentSerializer,
            400: 'اطلاعات نامعتبر',
            404: 'مدرک یافت نشد',
            401: 'احراز هویت نشده'
        }
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="حذف مدرک قانونی",
        responses={
            204: 'مدرک حذف شد',
            404: 'مدرک یافت نشد',
            401: 'احراز هویت نشده'
        }
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        operation_description='آپلود فایل (عکس، ویدیو، داکیومنت و ...)',
        manual_parameters=[
            openapi.Parameter(
                'file',
                openapi.IN_FORM,
                description='فایل برای آپلود',
                type=openapi.TYPE_FILE,
                required=True
            )
        ],
        responses={
            200: openapi.Response(
                description='آدرس فایل آپلود شده',
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'url': openapi.Schema(type=openapi.TYPE_STRING, description='آدرس فایل')
                    }
                )
            ),
            400: 'فایل نامعتبر'
        }
    )
    def post(self, request):
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.validated_data['file']
            file_name = default_storage.save(file.name, file)
            file_url = default_storage.url(file_name)
            return Response({'url': file_url})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_file(request):
    serializer = FileUploadSerializer(data=request.data)
    if serializer.is_valid():
        file = serializer.validated_data['file']
        file_name = default_storage.save(file.name, file)
        file_url = default_storage.url(file_name)
        return Response({'url': file_url})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class ProjectEmployeeView(APIView):
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        operation_description="دریافت کارمندان یک پروژه خاص",
        manual_parameters=[
            openapi.Parameter(
                'project_id',
                openapi.IN_PATH,
                description='شناسه پروژه',
                type=openapi.TYPE_INTEGER,
                required=True
            ),
            openapi.Parameter(
                'employee_id',
                openapi.IN_PATH,
                description='شناسه کارمند',
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        responses={
            200: EmployeeSerializer,
            404: 'پروژه یا کارمند یافت نشد',
            401: 'احراز هویت نشده'
        }
    )
    def get(self, request, project_id, employee_id):
        try:
            project = Project.objects.get(id=project_id)
            employee = Employee.objects.get(id=employee_id, project=project)
        except (Project.DoesNotExist, Employee.DoesNotExist):
            return Response({"detail": "Project or Employee not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data) 