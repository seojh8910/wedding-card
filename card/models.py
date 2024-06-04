from django.db import models

from account.models import User



# Create your models here.
class Card(models.Model):

    THEME_TYPE = [
        ('클래식', '클래식'),
        ('밤하늘', '밤하늘'),
    ]

    GROOM_POSITION = [
        ('아들', '아들'),
        ('장남', '장남'),
        ('차남', '차남'),
        ('삼남', '삼남'),
        ('사남', '사남'),
        ('독남', '독남'),
        ('막내', '막내'),
        ('조카', '조카'),
        ('손자', '손자'),
        ('동생', '동생'),
    ]

    BRIDE_POSITION = [
        ('딸', '딸'),
        ('장녀', '장녀'),
        ('차녀', '차녀'),
        ('삼녀', '삼녀'),
        ('사녀', '사녀'),
        ('독녀', '독녀'),
        ('막내', '막내'),
        ('조카', '조카'),
        ('손녀', '손녀'),
        ('동생', '동생'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='card', null=True)
    theme = models.CharField(max_length=20, choices=THEME_TYPE, default='클래식')  # 청첩장 테마

    wedding_date = models.DateTimeField(null=True, blank=True)  # 결혼식 날짜
    wedding_hall_name = models.CharField(max_length=100, null=True, blank=True)  # 예식장명
    wedding_hall_floor = models.CharField(max_length=100, null=True, blank=True)  # 예식장 층과 홀
    wedding_hall_address = models.CharField(max_length=100, null=True, blank=True)  # 예식장 주소
    main_img = models.ImageField(upload_to='card/main/', null=True, blank=True)  # 청첩장 메인 이미지

    groom_name = models.CharField(max_length=20, null=True, blank=True)  # 신랑 이름
    groom_mother_name = models.CharField(max_length=20, null=True, blank=True)  # 신랑 어머니 성함
    groom_father_name = models.CharField(max_length=20, null=True, blank=True)  # 신랑 아버지 성함
    groom_position = models.CharField(max_length=10, choices=GROOM_POSITION, default='아들')  # 신랑 호칭 ex) 아들, 장남, 차남 등

    bride_name = models.CharField(max_length=20, null=True, blank=True)  # 신부 이름
    bride_mother_name = models.CharField(max_length=20, null=True, blank=True)  # 신부 어머니 성함
    bride_father_name = models.CharField(max_length=20, null=True, blank=True)  # 신부 아버지 성함
    bride_position = models.CharField(max_length=10, choices=BRIDE_POSITION, default='딸')  # 신부 호칭 ex) 딸, 장녀, 차녀 등

    invitation_title = models.CharField(max_length=20, null=True, blank=True)  # 모시는 글 제목
    invitation_content = models.TextField(null=True, blank=True)  # 모시는 글 내용

    thumb_img = models.ImageField(upload_to='card/thumb/', null=True, blank=True)  # 썸네일 이미지
    thumb_title = models.CharField(max_length=20, null=True, blank=True)  # 썸네일 제목
    thumb_content = models.CharField(max_length=100, null=True, blank=True)  # 썸네일 내용

    guests_comment = models.CharField(max_length=20, null=True, default='temp')  # 하객 방명록

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)  # 청첩장 생성일
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)  # 청첩장 수정일

