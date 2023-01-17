from django.db import models
from django.contrib.auth.models import User
from chat.models import Chat


class custom_user (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='abstract-user.png', null= True, blank=True)
    gender = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=100, unique=True)
    chats = models.ForeignKey(Chat, on_delete=models.CASCADE, null=True)

# @receiver(post_save, sender=User)
# def create_custom_user(sender, instance, created, **kwargs):
#     if created:
#         custom_user.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_custom_user(sender, instance, **kwargs):
#     instance.custom_user.save()

# def update_profile(request, user_id):
#     user = User.objects.get(pk=user_id)
#     user.save() 
