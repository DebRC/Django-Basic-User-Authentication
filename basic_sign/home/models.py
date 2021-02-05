from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional fields
    profile_pic = models.ImageField(upload_to = 'profile_pics',blank=True)

    def __str__(self):
        return self.user.username