# Generated by Django 5.0.1 on 2024-04-09 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_user_username"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="username",),
    ]