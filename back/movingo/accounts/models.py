from math import radians
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from random import randint
# Create your models here.

    

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    def __str__(self):
        return self.username
    

class ProfileInfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile_info')
    profile_img = models.IntegerField(default=1)
    nickname=models.CharField(max_length=16)

    


