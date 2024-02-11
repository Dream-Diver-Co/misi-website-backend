# Generated by Django 5.0.2 on 2024-02-11 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misiBackend', '0004_profile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
