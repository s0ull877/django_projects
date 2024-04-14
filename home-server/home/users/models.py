from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    
    email = models.EmailField(_("email address"), blank=True, unique=True)
    image = models.ImageField(upload_to='users_images', blank=True, null=True)
    is_verified = models.BooleanField(default=False)
