from django.db import models

from account.models import User
from card.models import Card


# Create your models here.
class GuestBook(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='guestbooks')
    writer = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    content = models.TextField(null=False)
    created_at = models.DateField(auto_now_add=True)
