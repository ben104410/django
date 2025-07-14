from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('staff', 'Staff'),
        ('community', 'Community'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='community')

    @property
    def is_staff(self):
        return self.role == 'staff'
