import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prj.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

try:
    # حذف همه کاربران
    users = User.objects.all()
    count = users.count()
    users.delete()
    print(f'{count} user(s) deleted successfully!')
except Exception as e:
    print('Error:', str(e)) 