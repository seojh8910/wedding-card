from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    가입 유형은 4가지
    gmail, naver, kakao, basic
    """
    username = models.CharField(max_length=20, null=False)
    first_name = None
    last_name = None
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=30, null=False)
    type = models.CharField(max_length=30, null=False, default='basic')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []