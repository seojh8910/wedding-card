from django.db import models

from account.models import User


class Review(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    image = models.ImageField(upload_to='reviews')
    content = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
