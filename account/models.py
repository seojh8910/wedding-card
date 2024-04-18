from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    가입 유형은 4가지
    gmail, naver, kakao, basic
    """
    first_name = None
    last_name = None
    phone_number = models.CharField(max_length=30, null=False, unique=True)
    type = models.CharField(max_length=30, null=False, default='basic')
