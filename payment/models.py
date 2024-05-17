from django.db import models

from account.models import User


class Payment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payment')
    paid_amount = models.IntegerField(null=True)
    name = models.CharField(max_length=100, null=True)
    imp_uid = models.CharField(max_length=200)
    merchant_uid = models.CharField(max_length=200)
    pay_method = models.CharField(max_length=50)
    apply_num = models.CharField(max_length=200, null=True)
    pg_provider = models.CharField(max_length=100)
    buyer_name = models.CharField(max_length=200, null=True)
    buyer_email = models.CharField(max_length=200, null=True)
    pg_tid = models.CharField(max_length=200, null=True)
    receipt_url = models.CharField(max_length=250, null=True)
    card_name = models.CharField(max_length=200, null=True)
    card_number = models.CharField(max_length=200, null=True)
    success = models.CharField(max_length=100)
    status = models.CharField(max_length=100, null=True)
    paid_at = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

