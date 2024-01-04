from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .manager import MyUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=100)
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)


class Book(models.Model):
    title = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
