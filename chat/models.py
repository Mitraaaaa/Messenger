from django.db import models


class Chat (models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    type = models.CharField(max_length=10, default='Group')


class Message (models.Model):
    MSG_TXT = 'tx'
    MSG_MD = 'md'
    MSG_TYPE = [
        (MSG_MD, 'Media'),
        (MSG_TXT, 'Text'),
    ]
    sender = models.CharField(max_length=200, null=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=10, choices=MSG_TYPE, default=MSG_TXT)
    time = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=False, null=False)
    seen = models.BooleanField(default=False)

