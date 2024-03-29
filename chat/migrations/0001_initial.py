# Generated by Django 4.1.3 on 2022-12-25 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('DM', 'Private'), ('GP', 'Group'), ('CH', 'Channel')], default='DM', max_length=10)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('member', models.ManyToManyField(to='user.custom_user')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('md', 'Media'), ('tx', 'Text'), ('vc', 'Voice')], default='tx', max_length=10)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('seen', models.BooleanField(default=False)),
                ('chat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chat.chat')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.custom_user')),
            ],
        ),
    ]
