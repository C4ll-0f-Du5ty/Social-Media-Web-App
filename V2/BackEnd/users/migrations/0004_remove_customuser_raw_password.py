# Generated by Django 5.1.1 on 2024-09-26 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_raw_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='raw_password',
        ),
    ]