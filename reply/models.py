from django.contrib.auth.models import User
from django.db import models
from board.models import Board
from users.models import Users


class Comment(models.Model):
    nickname = models.CharField(max_length=50)
    contents = models.TextField()
    point_review = models.IntegerField(null=True, default='', blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    def __str__(self): return self.nickname
