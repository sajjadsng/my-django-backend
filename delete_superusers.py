import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prj.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

try:
    # حذف همه سوپریوزرها
    superusers = User.objects.filter(is_superuser=True)
    count = superusers.count()
    superusers.delete()
    print(f'{count} superuser(s) deleted successfully!')
except Exception as e:
    print('Error:', str(e)) 