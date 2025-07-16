# This file contains the WSGI configuration required to serve up your
# web application at http://sajjadsng.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#

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