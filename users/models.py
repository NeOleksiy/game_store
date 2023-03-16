from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    img = models.ImageField(upload_to='media/users_img', null=True, blank=True)

