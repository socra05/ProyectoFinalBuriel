# Generated by Django 4.2 on 2023-04-28 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0003_alter_avatar_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
