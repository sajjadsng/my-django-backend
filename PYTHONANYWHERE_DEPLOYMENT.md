# PythonAnywhere Deployment Guide

## مراحل Deploy روی PythonAnywhere

### 1. ثبت‌نام در PythonAnywhere
- به [pythonanywhere.com](https://www.pythonanywhere.com/) برید
- ثبت‌نام کنید (رایگان)

### 2. ایجاد Web App
1. **Dashboard** → **Web** → **Add a new web app**
2. **Domain name**: `sajjadsng.pythonanywhere.com`
3. **Python version**: Python 3.11
4. **Framework**: Manual configuration

### 3. کلون کردن پروژه
```bash
# در Bash console
cd ~
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 4. نصب Dependencies
```bash
pip install --user -r requirements.txt
```

### 5. تنظیم متغیرهای محیطی
در **Web** → **Code** → **Environment variables**:
```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=sajjadsng.pythonanywhere.com
CORS_ALLOW_ALL_ORIGINS=True
```

### 6. تنظیم WSGI Configuration
در **Web** → **Code** → **WSGI configuration file**:

```python
import os
import sys

# Add your project directory to the sys.path
path = '/home/sajjadsng/your-repo'
if path not in sys.path:
    sys.path.append(path)

# Set environment variables
os.environ['SECRET_KEY'] = 'your-secret-key-here'
os.environ['DEBUG'] = 'False'
os.environ['ALLOWED_HOSTS'] = 'sajjadsng.pythonanywhere.com'
os.environ['CORS_ALLOW_ALL_ORIGINS'] = 'True'

# Import Django settings
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prj.settings')
application = get_wsgi_application()
```

### 7. اجرای Migrations
```bash
# در Bash console
cd ~/your-repo
python manage.py migrate
python manage.py collectstatic --noinput
```

### 8. ایجاد Superuser (اختیاری)
```bash
python manage.py createsuperuser
```

### 9. Reload Web App
در **Web** → **Reload** کلیک کنید

## تنظیمات اضافی

### Static Files
در **Web** → **Static files**:
- **URL**: `/static/`
- **Directory**: `/home/sajjadsng/your-repo/staticfiles`

### Media Files
در **Web** → **Static files**:
- **URL**: `/media/`
- **Directory**: `/home/sajjadsng/your-repo/media`

## تست API

### API Root
```
https://sajjadsng.pythonanywhere.com/api/
```

### Swagger
```
https://sajjadsng.pythonanywhere.com/swagger/
```

### Register
```bash
curl -X POST https://sajjadsng.pythonanywhere.com/api/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "password123",
    "first_name": "Test",
    "last_name": "User",
    "mobile": "09123456789"
  }'
```

## مشکلات رایج

### 1. Import Error
- مطمئن شوید که path در WSGI درست تنظیم شده
- dependencies نصب شده باشند

### 2. 404 Error
- URL patterns درست تنظیم شده باشند
- migrations اجرا شده باشند

### 3. Static Files
- `collectstatic` اجرا شده باشد
- Static files در Web settings تنظیم شده باشند

### 4. Database
- SQLite برای free tier کافی است
- برای production از PostgreSQL استفاده کنید

## نکات مهم

1. **Free Tier محدودیت‌ها**:
   - CPU time محدود
   - Storage محدود
   - Custom domains پولی

2. **Security**:
   - `DEBUG=False` در production
   - `SECRET_KEY` امن
   - `ALLOWED_HOSTS` درست

3. **Performance**:
   - Static files را serve کنید
   - Database queries را optimize کنید
   - Caching استفاده کنید

## آپدیت کد

```bash
# در Bash console
cd ~/your-repo
git pull origin main
python manage.py migrate
python manage.py collectstatic --noinput
# سپس Reload کنید
``` 