import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prj.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

try:
    u = User.objects.get(username='admin5')
    u.is_superuser = True
    u.is_staff = True
    u.role = 'admin'
    u.set_password('admin123456')
    u.save()
    print('User fixed!')
    print('is_superuser:', u.is_superuser)
    print('is_staff:', u.is_staff)
    print('role:', u.role)
except Exception as e:
    print('Error:', str(e)) 