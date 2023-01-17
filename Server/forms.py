from django import forms
from django.contrib.auth.models import User
from user.models import custom_user

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30 , label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    phone_number = forms.CharField(max_length=10)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone_number = self.cleaned_data['phone_number']
        user.save()

