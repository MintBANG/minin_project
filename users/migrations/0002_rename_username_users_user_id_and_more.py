# Generated by Django 4.1.7 on 2023-03-08 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='username',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='password',
            new_name='user_pw',
        ),
    ]
