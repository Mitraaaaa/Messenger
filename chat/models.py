from django.db import models
from user.models import User


class Chat (models.Model):
    TYPE_DM = 'DM'
    TYPE_GP = 'GP'
    TYP_CH = 'CH'
    CHAT_TYPE = [
        (TYPE_DM, 'Private'),
        (TYPE_GP, 'Group'),
        (TYP_CH, 'Channel')
    ]
    type = models.CharField(max_length=10, choices=CHAT_TYPE, default=TYPE_DM)
    name = models.CharField(max_length=30, blank=True, null=True)
    # member = models.ManyToManyField(custom_user)


class Message (models.Model):
    MSG_TXT = 'tx'
    MSG_VC = 'vc'
    MSG_MD = 'md'
    MSG_TYPE = [
        (MSG_MD, 'Media'),
        (MSG_TXT, 'Text'),
        (MSG_VC, 'Voice')
    ]
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, null=True)
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)
    # TODO replied msg ID
    type = models.CharField(max_length=10, choices=MSG_TYPE, default=MSG_TXT)
    time = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=False, null=False)
    seen = models.BooleanField(default=False)
    # TODO upload_tool must be added
    attachment = models.FileField()
    def __str__(self):
        return self.message
