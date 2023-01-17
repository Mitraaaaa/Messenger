from django.shortcuts import render
from user.models import custom_user
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email , RegexValidator

def sign_up(request):
    return render(request , 'signup.html')
