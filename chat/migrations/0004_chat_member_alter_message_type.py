# Generated by Django 4.1.3 on 2023-01-15 16:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0003_alter_message_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='member',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Participant'),
        ),
        migrations.AlterField(
            model_name='message',
            name='type',
            field=models.CharField(choices=[('md', 'Media'), ('tx', 'Text')], default='tx', max_length=10),
        ),
    ]
