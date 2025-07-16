# API Guide for Frontend Team

## Base URLs

### Development (Local)
```
http://127.0.0.1:8000/api/
```

### Production (PythonAnywhere)
```
https://sajjadsng.pythonanywhere.com/api/
```

## Authentication

### Register
```javascript
POST /api/register/
{
  "email": "user@example.com",
  "password": "password123",
  "first_name": "نام",
  "last_name": "نام خانوادگی",
  "mobile": "09123456789"
}
```

### Login
```javascript
POST /api/login/
{
  "email": "user@example.com",
  "password": "password123"
}
```

### Logout
```javascript
POST /api/logout/
Authorization: Bearer YOUR_JWT_TOKEN
```

### Profile
```javascript
GET /api/profile/
Authorization: Bearer YOUR_JWT_TOKEN
```

## Projects

### List Projects
```javascript
GET /api/projects/
Authorization: Bearer YOUR_JWT_TOKEN
```

### Create Project
```javascript
POST /api/projects/
Authorization: Bearer YOUR_JWT_TOKEN
{
  "investorProfile": {
    "fullName": "شرکت توسعه ساختمان تهران",
    "legalId": "123456789",
    "phoneNumber": "02112345678",
    "email": "info@tehran-dev.com",
    "address": "تهران، خیابان ولیعصر، پلاک 123"
  },
  "legalInformation": {
    "buildingPermit": "مجوز ساختمان شماره 2024/123",
    "draftSeparation": "طرح تفکیک تایید شده",
    "municipalityInquiry": "استعلام شهرداری مثبت",
    "environmentalPermit": "مجوز محیط زیست صادر شده",
    "firePermit": "مجوز آتش‌نشانی تایید شده",
    "engineeringSystemPermit": "مجوز سیستم مهندسی"
  },
  "title": "مجتمع مسکونی پارک وی",
  "address": "تهران، منطقه 2، خیابان فرمانیه",
  "category": "مسکونی",
  "ownershipStatus": "مالکیت خصوصی",
  "landArea": "2500.00",
  "infrastructure": "1200.00",
  "numFloors": 15,
  "usageEachFloor": "طبقه 1-3: تجاری، طبقه 4-15: مسکونی",
  "structuralSkeleton": "اسکلت فلزی",
  "hvacSystems": "سیستم تهویه مرکزی",
  "foundationTypes": "فونداسیون عمیق",
  "wallSystems": "دیوارهای بتنی پیش‌ساخته",
  "insulationSystems": "عایق حرارتی و صوتی",
  "roofTypes": "سقف تیرچه بلوک",
  "mepSystems": "سیستم‌های مکانیکی، برقی و لوله‌کشی",
  "smartSystems": "سیستم هوشمند ساختمان",
  "projectStatus": 1,
  "description": "مجتمع مسکونی لوکس 15 طبقه",
  "startDate": "2024-03-01",
  "image": ""
}
```

### Get Project Details
```javascript
GET /api/projects/{id}/
Authorization: Bearer YOUR_JWT_TOKEN
```

### Update Project
```javascript
PUT /api/projects/{id}/
Authorization: Bearer YOUR_JWT_TOKEN
```

### Delete Project
```javascript
DELETE /api/projects/{id}/
Authorization: Bearer YOUR_JWT_TOKEN
```

## Employees

### List Employees
```javascript
GET /api/employees/
Authorization: Bearer YOUR_JWT_TOKEN
```

### Create Employee
```javascript
POST /api/employees/
Authorization: Bearer YOUR_JWT_TOKEN
{
  "fullName": "علی احمدی",
  "nationalCode": "1234567890",
  "birthDate": "1990-05-15",
  "gender": "male",
  "photo": "",
  "phoneNumber": "09123456789",
  "email": "ali.ahmadi@company.com",
  "address": "تهران، خیابان ولیعصر، پلاک 456",
  "position": "مهندس عمران",
  "role": "employee",
  "department": "فنی و مهندسی",
  "employmentType": "fullTime",
  "startDate": "2024-01-01",
  "endDate": null,
  "supervisor": null,
  "project": 4,
  "username": "ali.ahmadi",
  "password": "password123",
  "isActive": true
}
```

### Get Employee Details
```javascript
GET /api/employees/{id}/
Authorization: Bearer YOUR_JWT_TOKEN
```

### Update Employee
```javascript
PUT /api/employees/{id}/
Authorization: Bearer YOUR_JWT_TOKEN
```

### Delete Employee
```javascript
DELETE /api/employees/{id}/
Authorization: Bearer YOUR_JWT_TOKEN
```

## File Upload

### Upload File
```javascript
POST /api/upload/
Authorization: Bearer YOUR_JWT_TOKEN
Content-Type: multipart/form-data

Form Data:
- file: [file object]
```

Response:
```json
{
  "url": "/media/filename.jpg"
}
```

## Choice Fields

### Project Status
```javascript
GET /api/choices/project-status/
```

### Employment Type
```javascript
GET /api/choices/employment-type/
```

### Gender
```javascript
GET /api/choices/gender/
```

### Roles
```javascript
GET /api/choices/roles/
```

## Investor Profiles

### List Investor Profiles
```javascript
GET /api/investor-profiles/
Authorization: Bearer YOUR_JWT_TOKEN
```

### Create Investor Profile
```javascript
POST /api/investor-profiles/
Authorization: Bearer YOUR_JWT_TOKEN
{
  "fullName": "شرکت توسعه ساختمان تهران",
  "legalId": "123456789",
  "phoneNumber": "02112345678",
  "email": "info@tehran-dev.com",
  "address": "تهران، خیابان ولیعصر، پلاک 123"
}
```

## Legal Documents

### List Legal Documents
```javascript
GET /api/legal-documents/
Authorization: Bearer YOUR_JWT_TOKEN
```

### Create Legal Document
```javascript
POST /api/legal-documents/
Authorization: Bearer YOUR_JWT_TOKEN
{
  "buildingPermit": "مجوز ساختمان شماره 2024/123",
  "draftSeparation": "طرح تفکیک تایید شده",
  "municipalityInquiry": "استعلام شهرداری مثبت",
  "environmentalPermit": "مجوز محیط زیست صادر شده",
  "firePermit": "مجوز آتش‌نشانی تایید شده",
  "engineeringSystemPermit": "مجوز سیستم مهندسی"
}
```

## API Root

### Get All Endpoints
```javascript
GET /api/
```

Returns a list of all available endpoints.

## Swagger Documentation

### Development
```
http://127.0.0.1:8000/swagger/
```

### Production
```
https://sajjadsng.pythonanywhere.com/swagger/
```

## Error Handling

### Common Error Responses

#### 401 Unauthorized
```json
{
  "detail": "Authentication credentials were not provided."
}
```

#### 400 Bad Request
```json
{
  "field_name": ["Error message"]
}
```

#### 404 Not Found
```json
{
  "detail": "Not found."
}
```

## Environment Variables for Frontend

```javascript
// Development
const API_BASE_URL = 'http://127.0.0.1:8000/api/';
const SWAGGER_URL = 'http://127.0.0.1:8000/swagger/';

// Production
const API_BASE_URL = 'https://sajjadsng.pythonanywhere.com/api/';
const SWAGGER_URL = 'https://sajjadsng.pythonanywhere.com/swagger/';
```

## Notes

1. **Authentication**: All protected endpoints require JWT token in Authorization header
2. **File Upload**: Use multipart/form-data for file uploads
3. **Dates**: Use ISO format (YYYY-MM-DD) for date fields
4. **Project Status**: 1=فعال, 2=در حال پیشرفت, 3=غیرفعال
5. **Gender**: "male" or "female"
6. **Employment Type**: "fullTime", "partTime", "contractor", "consultant"
7. **Roles**: "admin", "manager", "employee"

## Testing

You can test all APIs using:
- Swagger UI: `/swagger/`
- Postman
- curl commands
- Frontend application 