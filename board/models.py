from django.db import models

from users.models import Users

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    writer = models.ForeignKey(Users, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to="image", blank=True)
    like = models.ManyToManyField(Users, related_name='likes', blank=True)
    def __str__(self) : return self.title


class BoardImage(models.Model):
    image_title = models.CharField(max_length=200)
    image = models.ImageField(null=True, upload_to="image", blank=True)


class Write(models.Model):
    title = models.CharField(max_length=200)
    appear = models.CharField(max_length=200)
    contents = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    writer = models.ForeignKey(Users, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to="image", blank=True)
    def __str__(self) : return self.title