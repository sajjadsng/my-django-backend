from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import (
    CustomUser, Project, Employee, InvestorProfile, LegalDocument, 
    EmergencyContact, EmployeeDocuments, ProjectStatus, EmploymentType, 
    Gender, Roles
)

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['email', 'fullName', 'password', 'role', 'companyName']
    
    def create(self, validated_data):
        # Set username to email if not provided
        if 'username' not in validated_data:
            validated_data['username'] = validated_data['email']
        user = CustomUser.objects.create_user(**validated_data)
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'fullName', 'role', 'companyName']

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

# New Serializers for Project Management
class InvestorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorProfile
        fields = '__all__'

class LegalDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalDocument
        fields = '__all__'

class EmergencyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyContact
        fields = '__all__'
        extra_kwargs = {
            'employee': {'required': False}
        }

class EmployeeDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDocuments
        fields = '__all__'
        extra_kwargs = {
            'employee': {'required': False}
        }

class EmployeeSerializer(serializers.ModelSerializer):
    emergencyContact = EmergencyContactSerializer(read_only=True)
    documents = EmployeeDocumentsSerializer(read_only=True)
    projects = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    supervisor = serializers.PrimaryKeyRelatedField(read_only=True)
    project = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Employee
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

class EmployeeCreateSerializer(serializers.ModelSerializer):
    emergencyContact = EmergencyContactSerializer(required=False)
    documents = EmployeeDocumentsSerializer(required=False)
    
    class Meta:
        model = Employee
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        emergency_contact_data = validated_data.pop('emergencyContact', None)
        documents_data = validated_data.pop('documents', None)
        
        employee = Employee.objects.create(**validated_data)
        
        if emergency_contact_data:
            EmergencyContact.objects.create(employee=employee, **emergency_contact_data)
        
        if documents_data:
            EmployeeDocuments.objects.create(employee=employee, **documents_data)
        
        return employee

class ProjectSerializer(serializers.ModelSerializer):
    investorProfile = InvestorProfileSerializer(read_only=True)
    legalInformation = LegalDocumentSerializer(read_only=True)
    employees = EmployeeSerializer(many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = '__all__'

class ProjectCreateSerializer(serializers.ModelSerializer):
    investorProfile = InvestorProfileSerializer()
    legalInformation = LegalDocumentSerializer()
    
    class Meta:
        model = Project
        fields = '__all__'
    
    def create(self, validated_data):
        investor_profile_data = validated_data.pop('investorProfile')
        legal_information_data = validated_data.pop('legalInformation')
        
        investor_profile = InvestorProfile.objects.create(**investor_profile_data)
        legal_information = LegalDocument.objects.create(**legal_information_data)
        
        project = Project.objects.create(
            investorProfile=investor_profile,
            legalInformation=legal_information,
            **validated_data
        )
        
        return project

# Choice Field Serializers for Enums
class ProjectStatusSerializer(serializers.Serializer):
    value = serializers.IntegerField()
    label = serializers.CharField()

class EmploymentTypeSerializer(serializers.Serializer):
    value = serializers.CharField()
    label = serializers.CharField()

class GenderSerializer(serializers.Serializer):
    value = serializers.CharField()
    label = serializers.CharField()

class RolesSerializer(serializers.Serializer):
    value = serializers.CharField()
    label = serializers.CharField() 

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField() 