from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=225)
    password = models.CharField(max_length=200,null=True)
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)
   

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()
