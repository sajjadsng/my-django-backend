import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prj.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()

try:
    superuser = User.objects.create_superuser(
        username='admin3',
        email='admin3@example.com',
        password='admin123456',
        role='admin'
    )
    print('Superuser created successfully!')
    print('Username:', superuser.username)
    print('Password: admin123456')
except IntegrityError:
    print('Superuser already exists!') 