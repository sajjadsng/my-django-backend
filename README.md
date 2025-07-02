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

### Fly.io (توصیه شده)

1. **نصب Fly CLI**
```bash
# macOS
brew install flyctl

# Windows
powershell -Command "iwr https://fly.io/install.ps1 -useb | iex"

# Linux
curl -L https://fly.io/install.sh | sh
```

2. **Login به Fly.io**
```bash
fly auth login
```

3. **ایجاد app**
```bash
fly launch
```

4. **تنظیم متغیرهای محیطی**
```bash
fly secrets set SECRET_KEY="your-secret-key-here"
fly secrets set DEBUG="False"
fly secrets set ALLOWED_HOSTS=".fly.dev"
fly secrets set CORS_ALLOW_ALL_ORIGINS="True"
```

5. **ایجاد database**
```bash
fly postgres create django-auth-db
fly postgres attach django-auth-db
```

6. **Deploy**
```bash
fly deploy
```

### Render (جایگزین)

1. **اتصال به GitHub**
   - پروژه را در GitHub push کنید
   - در Render، New Web Service ایجاد کنید
   - از GitHub connect کنید

2. **تنظیمات Render**
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python manage.py migrate && python manage.py collectstatic --noinput && gunicorn prj.wsgi:application`
   - **Environment**: Python 3.11

3. **متغیرهای محیطی**
   - `SECRET_KEY`: کلید امن Django (Render خودش تولید می‌کند)
   - `DEBUG`: False
   - `ALLOWED_HOSTS`: .onrender.com
   - `DATABASE_URL`: Render PostgreSQL URL (اتوماتیک)

4. **Database**
   - PostgreSQL database اضافه کنید
   - Render خودکار DATABASE_URL را تنظیم می‌کند

### Railway (جایگزین)

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
ALLOWED_HOSTS=your-app.fly.dev
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
├── fly.toml              # Fly.io configuration
├── Dockerfile            # Docker configuration
├── render.yaml           # Render configuration
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