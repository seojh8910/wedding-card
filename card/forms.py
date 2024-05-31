from django import forms
from django.forms import DateTimeInput

from card.models import Card


class CardCreationForm(forms.ModelForm):

    main_img = forms.ImageField(widget=forms.HiddenInput(), required=False, error_messages={'required': '사진을 첨부해주세요.'}, label='메인 이미지')
    wedding_hall_address = forms.CharField(widget=forms.HiddenInput(), max_length=200, label='예식장 주소')

    class Meta:
        model = Card
        fields = '__all__'
        exclude = ('user', 'guests_comment', 'wedding_hall_address', )
        widgets = {

            'wedding_date': forms.DateTimeInput(attrs={'class': 'inorder_txt', 'type': 'datetime-local'}),

            'invitation_title': forms.TextInput(attrs={'class': 'inorder_txt'}),
            'invitation_content': forms.Textarea(attrs={'class': 'te-textarea'}),

            'groom_name': forms.TextInput(attrs={'class': 'inorder_txt', 'placeholder': '성함'}),
            'groom_mother_name': forms.TextInput(attrs={'class': 'inorder_txt', 'placeholder': '성함'}),
            'groom_father_name': forms.TextInput(attrs={'class': 'inorder_txt', 'placeholder': '성함'}),
            'groom_position': forms.Select(attrs={'class': 'inorder_txt'}),

            'bride_name': forms.TextInput(attrs={'class': 'inorder_txt', 'placeholder': '성함'}),
            'bride_mother_name': forms.TextInput(attrs={'class': 'inorder_txt', 'placeholder': '성함'}),
            'bride_father_name': forms.TextInput(attrs={'class': 'inorder_txt', 'placeholder': '성함'}),
            'bride_position': forms.Select(attrs={'class': 'inorder_txt'}),

            'thumb_title': forms.TextInput(attrs={'class': 'inorder_txt', 'placeholder': '김신랑♥김신부 결혼합니다'}),
            'thumb_content': forms.Textarea(attrs={'class': 'inorder_txt', 'placeholder': '5월 30일 목요일 오후 1시 30분'}),

        }
        labels = {
            'theme': '테마',
            'wedding_date': '결혼식 날짜',
            'main_img': '메인 이미지',
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
        }
