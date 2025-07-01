# Django REST API Authentication System

یک سیستم احراز هویت کامل با Django REST Framework و JWT tokens.

## ویژگی‌ها

- ✅ ثبت‌نام کاربران
- ✅ ورود و خروج
- ✅ احراز هویت با JWT tokens
- ✅ پروفایل کاربر
- ✅ مستندات API با Swagger
- ✅ پشتیبانی از CORS
- ✅ آماده برای deployment

## تکنولوژی‌های استفاده شده

- **Django 5.2.1** - فریم‌ورک اصلی
- **Django REST Framework** - برای ساخت API
- **Simple JWT** - برای احراز هویت
- **Swagger/OpenAPI** - برای مستندات
- **PostgreSQL** - دیتابیس (production)
- **SQLite** - دیتابیس (development)

## نصب و راه‌اندازی

### پیش‌نیازها

- Python 3.11+
- pip
- virtualenv (اختیاری)

### مراحل نصب

1. **کلون کردن پروژه**
```bash
git clone <repository-url>
cd Back-end
```

2. **ایجاد محیط مجازی**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# یا
venv\Scripts\activate  # Windows
```

3. **نصب وابستگی‌ها**
```bash
pip install -r requirements.txt
```

4. **تنظیم متغیرهای محیطی**
```bash
cp .env.example .env
# فایل .env را ویرایش کنید
```

5. **اجرای migration ها**
```bash
python manage.py migrate
```

6. **اجرای سرور**
```bash
python manage.py runserver
```

## API Endpoints

### احراز هویت

| متد | آدرس | توضیحات |
|-----|------|---------|
| POST | `/api/register/` | ثبت‌نام کاربر جدید |
| POST | `/api/login/` | ورود کاربر |
| POST | `/api/logout/` | خروج کاربر |
| GET | `/api/profile/` | دریافت پروفایل کاربر |

### مستندات API

- **Swagger UI**: `http://localhost:8000/swagger/`
- **ReDoc**: `http://localhost:8000/redoc/`

## مثال‌های استفاده

### ثبت‌نام
```bash
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "Test123456",
    "first_name": "علی",
    "last_name": "محمدی",
    "mobile": "09123456789"
  }'
```

### ورود
```bash
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "Test123456"
  }'
```

### دریافت پروفایل
```bash
curl -X GET http://localhost:8000/api/profile/ \
  -H "Authorization: Bearer <access_token>"
```

## Deployment

### Railway

1. **اتصال به GitHub**
   - پروژه را در GitHub push کنید
   - در Railway، پروژه جدید ایجاد کنید
   - از GitHub connect کنید

2. **تنظیم متغیرهای محیطی**
   - `SECRET_KEY`: کلید امن Django
   - `DEBUG`: False
   - `ALLOWED_HOSTS`: دامنه Railway شما
   - `DATABASE_URL`: Railway PostgreSQL URL

3. **Deploy**
   - Railway به صورت خودکار deploy می‌کند

### متغیرهای محیطی مورد نیاز

```env
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=your-app.railway.app
DATABASE_URL=postgresql://...
```

## ساختار پروژه

```
Back-end/
├── api/                    # اپلیکیشن اصلی
│   ├── models.py          # مدل CustomUser
│   ├── views.py           # API views
│   ├── serializers.py     # Serializers
│   └── urls.py            # URL patterns
├── prj/                   # تنظیمات پروژه
│   ├── settings.py        # تنظیمات Django
│   ├── urls.py            # URL patterns اصلی
│   └── wsgi.py            # WSGI configuration
├── requirements.txt       # وابستگی‌ها
├── Procfile              # Railway configuration
├── runtime.txt           # Python version
└── README.md             # این فایل
```

## مشارکت

1. Fork کنید
2. Branch جدید ایجاد کنید (`git checkout -b feature/amazing-feature`)
3. تغییرات را commit کنید (`git commit -m 'Add amazing feature'`)
4. Push کنید (`git push origin feature/amazing-feature`)
5. Pull Request ایجاد کنید

## لایسنس

این پروژه تحت لایسنس MIT منتشر شده است.

## پشتیبانی

اگر سوال یا مشکلی دارید، لطفاً issue ایجاد کنید. 