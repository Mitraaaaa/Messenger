from django.db import models

# Create your models here.
class User ():
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200, unique=True)
    # other attributes