# Generated by Django 3.2.15 on 2024-09-12 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='like_count',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='profile_image',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='user_id',
        ),
    ]
