# Generated by Django 4.1.3 on 2023-01-16 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_chat_member_alter_message_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='member',
        ),
    ]
