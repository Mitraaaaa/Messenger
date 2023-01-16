from django.db import models
from django.contrib.auth.models import User


class custom_user (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField()
    gender = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=100, unique=True)
