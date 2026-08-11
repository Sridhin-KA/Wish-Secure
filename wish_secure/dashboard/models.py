from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CoupleProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="avatars/")
    favorite_color = models.CharField(max_length=20)
    is_owner = models.BooleanField(default=False)