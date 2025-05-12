# Django REST Framework Project

این پروژه یک API با استفاده از Django REST Framework است.

## راه‌اندازی پروژه

1. ایجاد محیط مجازی:
```bash
python -m venv venv
```

2. فعال‌سازی محیط مجازی:
- در Windows:
```bash
.\venv\Scripts\activate
```
- در Linux/Mac:
```bash
source venv/bin/activate
```

3. نصب وابستگی‌ها:
```bash
pip install -r requirements.txt
```

4. اجرای مایگریشن‌ها:
```bash
python manage.py migrate
```

5. اجرای سرور توسعه:
```bash
python manage.py runserver
```

سرور در آدرس `http://127.0.0.1:8000` در دسترس خواهد بود. 