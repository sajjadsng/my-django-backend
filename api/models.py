from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('employee', 'کارمند'),
        ('admin', 'مدیر'),
    )
    
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')
    created_at = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
