from django.urls import path
from . import views

urlpatterns = [
    # API Root
    path('', views.api_root, name='api-root'),
    
    # Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:id>/', views.UserProfileByIdView.as_view(), name='user-profile-by-id'),
    
    # InvestorProfile Management URLs
    path('investor-profiles/', views.InvestorProfileListCreateView.as_view(), name='investor-profile-list-create'),
    path('investor-profiles/<int:id>/', views.InvestorProfileDetailView.as_view(), name='investor-profile-detail'),
    
    # LegalDocument Management URLs
    path('legal-documents/', views.LegalDocumentListCreateView.as_view(), name='legal-document-list-create'),
    path('legal-documents/<int:id>/', views.LegalDocumentDetailView.as_view(), name='legal-document-detail'),
    
    # Project Management URLs
    path('projects/', views.ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:id>/', views.ProjectDetailView.as_view(), name='project-detail'),
    
    # Employee Management URLs
    path('employees/', views.EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:id>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    
    # Project Employee URL (example of two IDs with unique names)
    path('projects/<int:project_id>/employees/<int:employee_id>/', views.ProjectEmployeeView.as_view(), name='project-employee-detail'),
    
    # Choice Fields URLs
    path('choices/project-status/', views.project_status_choices, name='project-status-choices'),
    path('choices/employment-type/', views.employment_type_choices, name='employment-type-choices'),
    path('choices/gender/', views.gender_choices, name='gender-choices'),
    path('choices/roles/', views.roles_choices, name='roles-choices'),

    # File Upload URL
    path('upload/', views.FileUploadView.as_view(), name='upload-file'),
] 