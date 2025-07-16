#!/usr/bin/env python3
"""
Script to update all swagger responses in views.py to use custom error codes
"""

import re

def update_swagger_responses():
    with open('api/views.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update ProjectListCreateView
    content = re.sub(
        r'@swagger_auto_schema\(\s*operation_description="دریافت لیست پروژه‌ها",\s*responses=\{\s*200: ProjectSerializer\(many=True\),\s*401: \'احراز هویت نشده\'\s*\}',
        '@swagger_auto_schema(\n        operation_description="Get Projects List",\n        responses={\n            200: ProjectSerializer(many=True),\n            \'AS1005\': openapi.Response(description=\'AuthenticationRequired\'),\n        }',
        content
    )
    
    content = re.sub(
        r'@swagger_auto_schema\(\s*operation_description="ایجاد پروژه جدید",\s*request_body=ProjectCreateSerializer,\s*responses=\{\s*201: ProjectSerializer,\s*400: \'اطلاعات نامعتبر\',\s*401: \'احراز هویت نشده\'\s*\}',
        '@swagger_auto_schema(\n        operation_description="Create New Project",\n        request_body=ProjectCreateSerializer,\n        responses={\n            201: ProjectSerializer,\n            \'AS2002\': openapi.Response(description=\'InvalidProjectData\'),\n            \'AS1005\': openapi.Response(description=\'AuthenticationRequired\'),\n        }',
        content
    )
    
    # Update ProjectDetailView
    content = re.sub(
        r'@swagger_auto_schema\(\s*operation_description="دریافت جزئیات پروژه",\s*responses=\{\s*200: ProjectSerializer,\s*404: \'پروژه یافت نشد\',\s*401: \'احراز هویت نشده\'\s*\}',
        '@swagger_auto_schema(\n        operation_description="Get Project Details",\n        responses={\n            200: ProjectSerializer,\n            \'AS2001\': openapi.Response(description=\'ProjectNotFound\'),\n            \'AS1005\': openapi.Response(description=\'AuthenticationRequired\'),\n        }',
        content
    )
    
    content = re.sub(
        r'@swagger_auto_schema\(\s*operation_description="به‌روزرسانی پروژه",\s*request_body=ProjectSerializer,\s*responses=\{\s*200: ProjectSerializer,\s*400: \'اطلاعات نامعتبر\',\s*404: \'پروژه یافت نشد\',\s*401: \'احراز هویت نشده\'\s*\}',
        '@swagger_auto_schema(\n        operation_description="Update Project",\n        request_body=ProjectSerializer,\n        responses={\n            200: ProjectSerializer,\n            \'AS2002\': openapi.Response(description=\'InvalidProjectData\'),\n            \'AS2001\': openapi.Response(description=\'ProjectNotFound\'),\n            \'AS1005\': openapi.Response(description=\'AuthenticationRequired\'),\n        }',
        content
    )
    
    content = re.sub(
        r'@swagger_auto_schema\(\s*operation_description="حذف پروژه",\s*responses=\{\s*204: \'پروژه حذف شد\',\s*404: \'پروژه یافت نشد\',\s*401: \'احراز هویت نشده\'\s*\}',
        '@swagger_auto_schema(\n        operation_description="Delete Project",\n        responses={\n            204: \'Project Deleted Successfully\',\n            \'AS2001\': openapi.Response(description=\'ProjectNotFound\'),\n            \'AS1005\': openapi.Response(description=\'AuthenticationRequired\'),\n        }',
        content
    )
    
    # Update EmployeeListCreateView
    content = re.sub(
        r'@swagger_auto_schema\(\s*operation_description="دریافت لیست کارمندان",\s*responses=\{\s*200: EmployeeSerializer\(many=True\),\s*401: \'احراز هویت نشده\'\s*\}',
        '@swagger_auto_schema(\n        operation_description="Get Employees List",\n        responses={\n            200: EmployeeSerializer(many=True),\n            \'AS1005\': openapi.Response(description=\'AuthenticationRequired\'),\n        }',
        content
    )
    
    content = re.sub(
        r'@swagger_auto_schema\(\s*operation_description="ایجاد کارمند جدید",\s*request_body=EmployeeCreateSerializer,\s*responses=\{\s*201: EmployeeSerializer,\s*400: \'اطلاعات نامعتبر\',\s*401: \'احراز هویت نشده\'\s*\}',
        '@swagger_auto_schema(\n        operation_description="Create New Employee",\n        request_body=EmployeeCreateSerializer,\n        responses={\n            201: EmployeeSerializer,\n            \'AS3002\': openapi.Response(description=\'InvalidEmployeeData\'),\n            \'AS1005\': openapi.Response(description=\'AuthenticationRequired\'),\n        }',
        content
    )
    
    # Update EmployeeDetailView
    content = re.sub(
        r'@swagger_auto_schema\(\s*operation_description="دریافت جزئیات کارمند",\s*responses=\{\s*200: EmployeeSerializer,\s*404: \'کارمند یافت نشد\',\s*401: \'احراز هویت نشده\'\s*\}',
        '@swagger_auto_schema(\n        operation_description="Get Employee Details",\n        responses={\n            200: EmployeeSerializer,\n            \'AS3001\': openapi.Response(description=\'EmployeeNotFound\'),\n            \'AS1005\': openapi.Response(description=\'AuthenticationRequired\'),\n        }',
        content
    )
    
    content = re.sub(
        r'@swagger_auto_schema\(\s*operation_description="به‌روزرسانی کارمند",\s*request_body=EmployeeSerializer,\s*responses=\{\s*200: EmployeeSerializer,\s*400: \'اطلاعات نامعتبر\',\s*404: \'کارمند یافت نشد\',\s*401: \'احراز هویت نشده\'\s*\}',
        '@swagger_auto_schema(\n        operation_description="Update Employee",\n        request_body=EmployeeSerializer,\n        responses={\n            200: EmployeeSerializer,\n            \'AS3002\': openapi.Response(description=\'InvalidEmployeeData\'),\n            \'AS3001\': openapi.Response(description=\'EmployeeNotFound\'),\n            \'AS1005\': openapi.Response(description=\'AuthenticationRequired\'),\n        }',
        content
    )
    
    content = re.sub(
        r'@swagger_auto_schema\(\s*operation_description="حذف کارمند",\s*responses=\{\s*204: \'کارمند حذف شد\',\s*404: \'کارمند یافت نشد\',\s*401: \'احراز هویت نشده\'\s*\}',
        '@swagger_auto_schema(\n        operation_description="Delete Employee",\n        responses={\n            204: \'Employee Deleted Successfully\',\n            \'AS3001\': openapi.Response(description=\'EmployeeNotFound\'),\n            \'AS1005\': openapi.Response(description=\'AuthenticationRequired\'),\n        }',
        content
    )
    
    # Update InvestorProfileListCreateView
    content = re.sub(
        r'@swagger_auto_schema\(\s*operation_description="دریافت لیست پروفایل‌های سرمایه‌گذار",\s*responses=\{\s*200: InvestorProfileSerializer\(many=True\),\s*401: \'احراز هویت نشده\'\s*\}',
        '@swagger_auto_schema(\n        operation_description="Get Investor Profiles List",\n        responses={\n            200: InvestorProfileSerializer(many=True),\n            \'AS1005\': openapi.Response(description=\'AuthenticationRequired\'),\n        }',
        content
    )
    
    content = re.sub(
        r'@swagger_auto_schema\(\s*operation_description="ایجاد پروفایل سرمایه‌گذار جدید",\s*request_body=InvestorProfileSerializer,\s*responses=\{\s*201: InvestorProfileSerializer,\s*400: \'اطلاعات نامعتبر\',\s*401: \'احراز هویت نشده\'\s*\}',
        '@swagger_auto_schema(\n        operation_description="Create New Investor Profile",\n        request_body=InvestorProfileSerializer,\n        responses={\n            201: InvestorProfileSerializer,\n            \'AS4002\': openapi.Response(description=\'InvalidInvestorData\'),\n            \'AS1005\': openapi.Response(description=\'AuthenticationRequired\'),\n        }',
        content
    )
    
    # Update InvestorProfileDetailView
    content = re.sub(
        r'@swagger_auto_schema\(\s*operation_description="دریافت جزئیات پروفایل سرمایه‌گذار",\s*responses=\{\s*200: InvestorProfileSerializer,\s*404: \'پروفایل یافت نشد\',\s*401: \'احراز هویت نشده\'\s*\}',
        '@swagger_auto_schema(\n        operation_description="Get Investor Profile Details",\n        responses={\n            200: InvestorProfileSerializer,\n            \'AS4001\': openapi.Response(description=\'InvestorProfileNotFound\'),\n            \'AS1005\': openapi.Response(description=\'AuthenticationRequired\'),\n        }',
        content
    )
    
    content = re.sub(
        r'@swagger_auto_schema\(\s*operation_description="به‌روزرسانی پروفایل سرمایه‌گذار",\s*request_body=InvestorProfileSerializer,\s*responses=\{\s*200: InvestorProfileSerializer,\s*400: \'اطلاعات نامعتبر\',\s*404: \'پروفایل یافت نشد\',\s*401: \'احراز هویت نشده\'\s*\}',
        '@swagger_auto_schema(\n        operation_description="Update Investor Profile",\n        request_body=InvestorProfileSerializer,\n        responses={\n            200: InvestorProfileSerializer,\n            \'AS4002\': openapi.Response(description=\'InvalidInvestorData\'),\n            \'AS4001\': openapi.Response(description=\'InvestorProfileNotFound\'),\n            \'AS1005\': openapi.Response(description=\'AuthenticationRequired\'),\n        }',
        content
    )
    
    content = re.sub(
        r'@swagger_auto_schema\(\s*operation_description="حذف پروفایل سرمایه‌گذار",\s*responses=\{\s*204: \'پروفایل حذف شد\',\s*404: \'پروفایل یافت نشد\',\s*401: \'احراز هویت نشده\'\s*\}',
        '@swagger_auto_schema(\n        operation_description="Delete Investor Profile",\n        responses={\n            204: \'Investor Profile Deleted Successfully\',\n            \'AS4001\': openapi.Response(description=\'InvestorProfileNotFound\'),\n            \'AS1005\': openapi.Response(description=\'AuthenticationRequired\'),\n        }',
        content
    )
    
    # Update LegalDocumentListCreateView
    content = re.sub(
        r'@swagger_auto_schema\(\s*operation_description="دریافت لیست مدارک قانونی",\s*responses=\{\s*200: LegalDocumentSerializer\(many=True\),\s*401: \'احراز هویت نشده\'\s*\}',
        '@swagger_auto_schema(\n        operation_description="Get Legal Documents List",\n        responses={\n            200: LegalDocumentSerializer(many=True),\n            \'AS1005\': openapi.Response(description=\'AuthenticationRequired\'),\n        }',
        content
    )
    
    content = re.sub(
        r'@swagger_auto_schema\(\s*operation_description="ایجاد مدرک قانونی جدید",\s*request_body=LegalDocumentSerializer,\s*responses=\{\s*201: LegalDocumentSerializer,\s*400: \'اطلاعات نامعتبر\',\s*401: \'احراز هویت نشده\'\s*\}',
        '@swagger_auto_schema(\n        operation_description="Create New Legal Document",\n        request_body=LegalDocumentSerializer,\n        responses={\n            201: LegalDocumentSerializer,\n            \'AS5002\': openapi.Response(description=\'InvalidDocumentData\'),\n            \'AS1005\': openapi.Response(description=\'AuthenticationRequired\'),\n        }',
        content
    )
    
    # Update LegalDocumentDetailView
    content = re.sub(
        r'@swagger_auto_schema\(\s*operation_description="دریافت جزئیات مدرک قانونی",\s*responses=\{\s*200: LegalDocumentSerializer,\s*404: \'مدرک یافت نشد\',\s*401: \'احراز هویت نشده\'\s*\}',
        '@swagger_auto_schema(\n        operation_description="Get Legal Document Details",\n        responses={\n            200: LegalDocumentSerializer,\n            \'AS5001\': openapi.Response(description=\'LegalDocumentNotFound\'),\n            \'AS1005\': openapi.Response(description=\'AuthenticationRequired\'),\n        }',
        content
    )
    
    content = re.sub(
        r'@swagger_auto_schema\(\s*operation_description="به‌روزرسانی مدرک قانونی",\s*request_body=LegalDocumentSerializer,\s*responses=\{\s*200: LegalDocumentSerializer,\s*400: \'اطلاعات نامعتبر\',\s*404: \'مدرک یافت نشد\',\s*401: \'احراز هویت نشده\'\s*\}',
        '@swagger_auto_schema(\n        operation_description="Update Legal Document",\n        request_body=LegalDocumentSerializer,\n        responses={\n            200: LegalDocumentSerializer,\n            \'AS5002\': openapi.Response(description=\'InvalidDocumentData\'),\n            \'AS5001\': openapi.Response(description=\'LegalDocumentNotFound\'),\n            \'AS1005\': openapi.Response(description=\'AuthenticationRequired\'),\n        }',
        content
    )
    
    content = re.sub(
        r'@swagger_auto_schema\(\s*operation_description="حذف مدرک قانونی",\s*responses=\{\s*204: \'مدرک حذف شد\',\s*404: \'مدرک یافت نشد\',\s*401: \'احراز هویت نشده\'\s*\}',
        '@swagger_auto_schema(\n        operation_description="Delete Legal Document",\n        responses={\n            204: \'Legal Document Deleted Successfully\',\n            \'AS5001\': openapi.Response(description=\'LegalDocumentNotFound\'),\n            \'AS1005\': openapi.Response(description=\'AuthenticationRequired\'),\n        }',
        content
    )
    
    # Update FileUploadView
    content = re.sub(
        r'@swagger_auto_schema\(\s*operation_description=\'آپلود فایل \(عکس، ویدیو، داکیومنت و \.\.\.\)\',\s*manual_parameters=\[\s*openapi\.Parameter\(\s*\'file\',\s*openapi\.IN_FORM,\s*description=\'فایل برای آپلود\',\s*type=openapi\.TYPE_FILE,\s*required=True\s*\)\s*\],\s*responses=\{\s*200: openapi\.Response\(\s*description=\'آدرس فایل آپلود شده\',\s*schema=openapi\.Schema\(\s*type=openapi\.TYPE_OBJECT,\s*properties=\{\s*\'url\': openapi\.Schema\(type=openapi\.TYPE_STRING, description=\'آدرس فایل\'\)\s*\}\s*\)\s*\),\s*400: \'فایل نامعتبر\'\s*\}',
        '@swagger_auto_schema(\n        operation_description=\'Upload File (Image, Video, Document, etc.)\',\n        manual_parameters=[\n            openapi.Parameter(\n                \'file\',\n                openapi.IN_FORM,\n                description=\'File to upload\',\n                type=openapi.TYPE_FILE,\n                required=True\n            )\n        ],\n        responses={\n            200: openapi.Response(\n                description=\'File Uploaded Successfully\',\n                schema=openapi.Schema(\n                    type=openapi.TYPE_OBJECT,\n                    properties={\n                        \'url\': openapi.Schema(type=openapi.TYPE_STRING, description=\'File URL\')\n                    }\n                )\n            ),\n            \'AS6001\': openapi.Response(description=\'FileUploadFailed\'),\n            \'AS6002\': openapi.Response(description=\'InvalidFileType\'),\n            \'AS6003\': openapi.Response(description=\'FileTooLarge\'),\n        }',
        content
    )
    
    # Update ProjectEmployeeView
    content = re.sub(
        r'@swagger_auto_schema\(\s*operation_description="دریافت کارمندان یک پروژه خاص",\s*manual_parameters=\[\s*openapi\.Parameter\(\s*\'project_id\',\s*openapi\.IN_PATH,\s*description=\'شناسه پروژه\',\s*type=openapi\.TYPE_INTEGER,\s*required=True\s*\),\s*openapi\.Parameter\(\s*\'employee_id\',\s*openapi\.IN_PATH,\s*description=\'شناسه کارمند\',\s*type=openapi\.TYPE_INTEGER,\s*required=True\s*\)\s*\],\s*responses=\{\s*200: EmployeeSerializer,\s*404: \'پروژه یا کارمند یافت نشد\',\s*401: \'احراز هویت نشده\'\s*\}',
        '@swagger_auto_schema(\n        operation_description="Get Employee of Specific Project",\n        manual_parameters=[\n            openapi.Parameter(\n                \'project_id\',\n                openapi.IN_PATH,\n                description=\'Project ID\',\n                type=openapi.TYPE_INTEGER,\n                required=True\n            ),\n            openapi.Parameter(\n                \'employee_id\',\n                openapi.IN_PATH,\n                description=\'Employee ID\',\n                type=openapi.TYPE_INTEGER,\n                required=True\n            )\n        ],\n        responses={\n            200: EmployeeSerializer,\n            \'AS2001\': openapi.Response(description=\'ProjectNotFound\'),\n            \'AS3001\': openapi.Response(description=\'EmployeeNotFound\'),\n            \'AS1005\': openapi.Response(description=\'AuthenticationRequired\'),\n        }',
        content
    )
    
    with open('api/views.py', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ All swagger responses updated successfully!")

if __name__ == "__main__":
    update_swagger_responses() 