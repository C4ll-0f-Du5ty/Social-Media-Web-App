# Generated by Django 5.1.1 on 2024-09-30 20:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='friend_request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.friendrequest'),
        ),
    ]
