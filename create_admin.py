import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prj.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()

try:
    existing = User.objects.filter(username='admin')
    if existing.exists():
        existing.delete()
        print('Old user deleted.')
    user = User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='admin123456',
        role='admin'
    )
    print('Superuser created successfully!')
    print('Username: admin')
    print('Password: admin123456')
except Exception as e:
    print('Error:', str(e)) 