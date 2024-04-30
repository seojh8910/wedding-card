from django.db import models

from account.models import User


class Board(models.Model):

    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='board')
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=100)
    is_secret = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='comment')
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    content = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
