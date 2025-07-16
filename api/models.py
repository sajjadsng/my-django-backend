from django.contrib.auth.models import AbstractUser
from django.db import models

# Enums
class ProjectStatus(models.IntegerChoices):
    ACTIVE = 1, 'فعال'
    IN_PROGRESS = 2, 'در حال پیشرفت'
    INACTIVE = 3, 'غیرفعال'

class EmploymentType(models.TextChoices):
    FULL_TIME = 'fullTime', 'تمام وقت'
    PART_TIME = 'partTime', 'نیمه وقت'
    CONTRACTOR = 'contractor', 'پیمانکار'
    CONSULTANT = 'consultant', 'مشاور'

class Gender(models.TextChoices):
    MALE = 'male', 'مرد'
    FEMALE = 'female', 'زن'

class Roles(models.TextChoices):
    ADMIN = 'admin', 'مدیر'
    EMPLOYEE = 'employee', 'کارمند'

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    fullName = models.CharField(max_length=255, verbose_name='نام کامل', default='No Name')
    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.EMPLOYEE, verbose_name='نقش')
    companyName = models.CharField(max_length=255, blank=True, null=True, verbose_name='نام شرکت')
    username = models.CharField(max_length=150, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullName']
    
    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)

# Models
class InvestorProfile(models.Model):
    fullName = models.CharField(max_length=255, verbose_name='نام کامل')
    legalId = models.CharField(max_length=50, verbose_name='شناسه قانونی')
    phoneNumber = models.CharField(max_length=20, verbose_name='شماره تلفن')
    email = models.EmailField(verbose_name='ایمیل')
    address = models.TextField(verbose_name='آدرس')
    
    def __str__(self):
        return self.fullName
    
    class Meta:
        verbose_name = 'پروفایل سرمایه‌گذار'
        verbose_name_plural = 'پروفایل‌های سرمایه‌گذار'

class LegalDocument(models.Model):
    buildingPermit = models.CharField(max_length=500, blank=True, null=True, verbose_name='مجوز ساختمان')
    draftSeparation = models.CharField(max_length=500, blank=True, null=True, verbose_name='طرح تفکیک')
    municipalityInquiry = models.CharField(max_length=500, blank=True, null=True, verbose_name='استعلام شهرداری')
    environmentalPermit = models.CharField(max_length=500, blank=True, null=True, verbose_name='مجوز محیط زیست')
    firePermit = models.CharField(max_length=500, blank=True, null=True, verbose_name='مجوز آتش‌نشانی')
    engineeringSystemPermit = models.CharField(max_length=500, blank=True, null=True, verbose_name='مجوز سیستم مهندسی')
    
    def __str__(self):
        return f"مدارک قانونی - {self.id}"
    
    class Meta:
        verbose_name = 'مدارک قانونی'
        verbose_name_plural = 'مدارک قانونی'

class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان پروژه')
    address = models.TextField(verbose_name='آدرس')
    category = models.CharField(max_length=100, verbose_name='دسته‌بندی')
    ownershipStatus = models.CharField(max_length=100, verbose_name='وضعیت مالکیت')
    landArea = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='مساحت زمین')
    infrastructure = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='زیرساخت')
    numFloors = models.IntegerField(verbose_name='تعداد طبقات')
    usageEachFloor = models.TextField(verbose_name='کاربری هر طبقه')
    investorProfile = models.ForeignKey(InvestorProfile, on_delete=models.CASCADE, verbose_name='پروفایل سرمایه‌گذار')
    legalInformation = models.ForeignKey(LegalDocument, on_delete=models.CASCADE, verbose_name='اطلاعات قانونی')
    structuralSkeleton = models.CharField(max_length=100, verbose_name='اسکلت سازه')
    hvacSystems = models.CharField(max_length=100, verbose_name='سیستم‌های تهویه')
    foundationTypes = models.CharField(max_length=100, verbose_name='نوع فونداسیون')
    wallSystems = models.CharField(max_length=100, verbose_name='سیستم دیوارها')
    insulationSystems = models.CharField(max_length=100, verbose_name='سیستم عایق‌بندی')
    roofTypes = models.CharField(max_length=100, verbose_name='نوع سقف')
    mepSystems = models.CharField(max_length=100, verbose_name='سیستم‌های MEP')
    smartSystems = models.CharField(max_length=100, verbose_name='سیستم‌های هوشمند')
    projectStatus = models.IntegerField(choices=ProjectStatus.choices, default=ProjectStatus.INACTIVE, verbose_name='وضعیت پروژه')
    description = models.TextField(verbose_name='توضیحات')
    startDate = models.DateField(verbose_name='تاریخ شروع')
    image = models.CharField(max_length=500, blank=True, null=True, verbose_name='تصویر پروژه')
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه‌ها'

class Employee(models.Model):
    fullName = models.CharField(max_length=255, verbose_name='نام کامل')
    nationalCode = models.CharField(max_length=20, unique=True, verbose_name='کد ملی')
    birthDate = models.DateField(blank=True, null=True, verbose_name='تاریخ تولد')
    gender = models.CharField(max_length=10, choices=Gender.choices, verbose_name='جنسیت')
    photo = models.CharField(max_length=500, blank=True, null=True, verbose_name='عکس')
    phoneNumber = models.CharField(max_length=20, blank=True, null=True, verbose_name='شماره تلفن')
    email = models.EmailField(blank=True, null=True, verbose_name='ایمیل')
    address = models.TextField(blank=True, null=True, verbose_name='آدرس')
    position = models.CharField(max_length=100, verbose_name='سمت')
    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.EMPLOYEE, verbose_name='نقش')
    department = models.CharField(max_length=100, blank=True, null=True, verbose_name='بخش')
    employmentType = models.CharField(max_length=20, choices=EmploymentType.choices, verbose_name='نوع استخدام')
    startDate = models.DateField(verbose_name='تاریخ شروع')
    endDate = models.DateField(blank=True, null=True, verbose_name='تاریخ پایان')
    supervisor = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='سرپرست')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='پروژه')
    username = models.CharField(max_length=50, blank=True, null=True, verbose_name='نام کاربری')
    password = models.CharField(max_length=128, blank=True, null=True, verbose_name='رمز عبور')
    isActive = models.BooleanField(default=True, verbose_name='فعال')
    projects = models.ManyToManyField(Project, related_name='employees', blank=True, verbose_name='پروژه‌ها')
    
    def __str__(self):
        return self.fullName
    
    class Meta:
        verbose_name = 'کارمند'
        verbose_name_plural = 'کارمندان'

class EmergencyContact(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='emergencyContact', verbose_name='کارمند')
    name = models.CharField(max_length=255, verbose_name='نام')
    relation = models.CharField(max_length=100, verbose_name='نسبت')
    phoneNumber = models.CharField(max_length=20, verbose_name='شماره تلفن')
    
    def __str__(self):
        return f"{self.name} - {self.employee.fullName}"
    
    class Meta:
        verbose_name = 'اطلاعات تماس اضطراری'
        verbose_name_plural = 'اطلاعات تماس اضطراری'

class EmployeeDocuments(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='documents', verbose_name='کارمند')
    nationalIdCard = models.CharField(max_length=500, blank=True, null=True, verbose_name='کارت ملی')
    resume = models.CharField(max_length=500, blank=True, null=True, verbose_name='رزومه')
    insuranceRecord = models.CharField(max_length=500, blank=True, null=True, verbose_name='سابقه بیمه')
    degreeCertificate = models.CharField(max_length=500, blank=True, null=True, verbose_name='مدرک تحصیلی')
    workLicense = models.CharField(max_length=500, blank=True, null=True, verbose_name='مجوز کار')
    
    def __str__(self):
        return f"مدارک {self.employee.fullName}"
    
    class Meta:
        verbose_name = 'مدارک کارمند'
        verbose_name_plural = 'مدارک کارمندان' 