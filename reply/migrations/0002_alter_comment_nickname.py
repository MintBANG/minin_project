# Generated by Django 4.1.7 on 2023-03-08 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reply', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='nickname',
            field=models.CharField(max_length=50),
        ),
    ]
