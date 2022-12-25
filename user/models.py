from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class custom_user (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="user")
    gender = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=100)