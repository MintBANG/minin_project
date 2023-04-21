# Generated by Django 4.1.7 on 2023-03-08 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=15)),
                ('contents', models.TextField()),
                ('point_review', models.IntegerField(blank=True, default='', null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.board')),
            ],
        ),
    ]
