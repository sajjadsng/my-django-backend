#!/usr/bin/env python
"""
Health check script for Render deployment
"""
import os
import sys
import django

def main():
    """Run health check."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prj.settings')
    django.setup()
    
    try:
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        print("Database connection: OK")
        
        from django.contrib.auth import get_user_model
        User = get_user_model()
        print("Django setup: OK")
        
        return 0
    except Exception as e:
        print(f"Health check failed: {e}")
        return 1

if __name__ == '__main__':
    sys.exit(main()) 