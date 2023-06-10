from django.db import models

# Create your models here.
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser



class CustomUserManager(BaseUserManager):

    def create_user(self,email,password,**extra_fields):
        email=self.normalize_email(email=email)
        user = self.model(
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password,**extra_fields):
        pass


class User(AbstractUser):
    pass 