# Generated by Django 5.1.1 on 2024-09-27 07:32

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_customuser_raw_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmessage',
            name='file',
        ),
        migrations.RemoveField(
            model_name='chatmessage',
            name='thread',
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='receiver',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='content',
            field=models.TextField(default='No content'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='sender',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL),
        ),
    ]