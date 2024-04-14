from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    image = models.ImageField(upload_to='users_images', blank=True, null=True)
    is_verified = models.BooleanField(default=False)
