# راهنمای حل مشکلات دیپلوی PythonAnywhere

## مشکلات فعلی و راه‌حل‌ها

### 1. مشکل IndentationError در فایل WSGI
**مشکل:** خطای indentation در فایل WSGI
**راه‌حل:** فایل WSGI را با محتوای زیر جایگزین کنید:

```python
import os
import sys

# Add your project directory to the sys.path
path = '/home/sajjadsng/my-django-backend'
if path not in sys.path:
    sys.path.append(path)

# Set environment variables
os.environ['SECRET_KEY'] = 'django-insecure-your-secret-key-here-change-this-in-production'
os.environ['DEBUG'] = 'False'
os.environ['ALLOWED_HOSTS'] = 'sajjadsng.pythonanywhere.com'
os.environ['CORS_ALLOW_ALL_ORIGINS'] = 'True'

# Import Django settings
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prj.settings')
application = get_wsgi_application()
```

### 2. مشکل ALLOWED_HOSTS
**مشکل:** `sajjadsng.pythonanywhere.com` در ALLOWED_HOSTS نیست
**راه‌حل:** فایل `prj/settings.py` آپدیت شده است

### 3. مشکل UserProfileByIdView
**مشکل:** URL pattern با view مطابقت ندارد
**راه‌حل:** فایل `api/urls.py` آپدیت شده است

## مراحل دیپلوی مجدد

### مرحله 1: آپلود فایل‌های جدید
1. فایل‌های آپدیت شده را روی PythonAnywhere آپلود کنید
2. مطمئن شوید که فایل‌های زیر آپدیت شده‌اند:
   - `prj/settings.py`
   - `api/urls.py`
   - `api/views.py`

### مرحله 2: نصب بسته‌های مورد نیاز
در Bash console روی PythonAnywhere:

```bash
cd /home/sajjadsng/my-django-backend
source venv/bin/activate
pip install -r requirements.txt
```

### مرحله 3: اجرای migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### مرحله 4: جمع‌آوری static files
```bash
python manage.py collectstatic --noinput
```

### مرحله 5: تنظیم فایل WSGI
1. در PythonAnywhere، به بخش "Web" بروید
2. روی "Code" کلیک کنید
3. فایل WSGI را با محتوای بالا جایگزین کنید
4. روی "Save" کلیک کنید

### مرحله 6: Reload وب‌سایت
1. در بخش "Web"، روی "Reload" کلیک کنید
2. چند ثانیه صبر کنید تا سرور restart شود

## بررسی مشکلات

### بررسی لاگ‌ها
1. در بخش "Web"، روی "Log files" کلیک کنید
2. فایل‌های error log را بررسی کنید

### تست API
پس از دیپلوی موفق، این URLها باید کار کنند:
- `https://sajjadsng.pythonanywhere.com/api/`
- `https://sajjadsng.pythonanywhere.com/swagger/`
- `https://sajjadsng.pythonanywhere.com/api/register/`
- `https://sajjadsng.pythonanywhere.com/api/login/`

## نکات مهم

1. **Secret Key:** حتماً SECRET_KEY را در production تغییر دهید
2. **Debug Mode:** در production باید DEBUG=False باشد
3. **Database:** اگر از SQLite استفاده می‌کنید، مطمئن شوید که فایل db.sqlite3 قابل نوشتن است
4. **Static Files:** مطمئن شوید که STATIC_ROOT درست تنظیم شده است

## مشکلات احتمالی و راه‌حل‌ها

### مشکل 404
- مطمئن شوید که URL patterns درست هستند
- فایل `prj/urls.py` را بررسی کنید

### مشکل Import Error
- مطمئن شوید که همه بسته‌ها نصب شده‌اند
- virtual environment فعال است

### مشکل Permission Denied
- مطمئن شوید که فایل‌ها قابل خواندن هستند
- مجوزهای فایل‌ها را بررسی کنید

## تماس با پشتیبانی

اگر مشکلات همچنان ادامه دارند:
1. لاگ‌های خطا را کپی کنید
2. وضعیت فایل‌ها را بررسی کنید
3. با تیم پشتیبانی تماس بگیرید 