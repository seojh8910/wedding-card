from django import forms
from django.forms import NumberInput

from card.models import Card


class CardCreationForm(forms.ModelForm):

    main_img = forms.ImageField(error_messages={'required': '사진을 첨부해주세요.'}, label='메인 이미지')
    wedding_date = forms.DateTimeField(widget=NumberInput(attrs={'type': 'date'}), label='결혼식 날짜')

    class Meta:
        model = Card
        fields = '__all__'
        exclude = ('user', )
        labels = {
            'theme': '테마',
            'wedding_date': '결혼식 날짜',
            'wedding_hall_address': '예식장 주소',
            'main_img': '메인 이미지',
            'invitation_title': '모시는 글 제목',
            'invitation_comment': '모시는 글 내용',
            'groom_name': '신랑님',
            'groom_mother_name': '신랑 어머님',
            'groom_father_name': '신랑 아버님',
            'groom_position': '신랑님 호칭',
            'bride_name': '신부님',
            'bride_mother_name': '신부 어머님',
            'bride_father_name': '신부 아버님',
            'bride_position': '신부님 호칭',
            'invitation_title': '모시는 글 제목',
            'invitation_content': '모시는 글 내용',
            'thumb_img': '썸네일 이미지',
            'thumb_title': '썸네일 제목',
            'thumb_content': '썸네일 내용',
            'guests_comment': '하객 방명록',
        }
