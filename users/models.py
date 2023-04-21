from django.db import models

# Create your models here.
class Users(models.Model):
    user_id = models.CharField(max_length=20)
    user_pw = models.CharField(max_length=200)
