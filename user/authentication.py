# TODO Custom authentication goes here
from .models import custom_user
from django.contrib.auth.backends import BaseBackend

class PhoneAuthBackend(BaseBackend):
    # more arguements to be added
    def authenticate(self, request, username=None, password=None):
        try:
            user = custom_user.objects.get(phone_number=username)
            if user.check_password(password):
                return user
            else:
                None
        except custom_user.DoesNotExist:
            return None

    def get_user(self, user_id) -> custom_user:
        try:
            return custom_user.objects.get(pk=user_id)
        except custom_user.DoesNotExist:
            return None
