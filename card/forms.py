from django import forms

from card.models import Card


class CardCreationForm(forms.ModelForm):

    main_img = forms.ImageField(error_messages={'required': '사진을 첨부해주세요.'}, label='메인 이미지')
    wedding_hall_address = forms.CharField(max_length=200, label='예식장 주소')

    class Meta:
        model = Card
        fields = '__all__'
        exclude = ('user', 'guests_comment', 'wedding_hall_address', )
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

    def __init__(self, *args, **kwargs):
        super(CardCreationForm, self).__init__(*args, **kwargs)

        # wedding_hall_address 필드 숨김 처리
        for field_name, field in self.fields.items():
            if field_name == 'wedding_hall_address':
                field.widget = forms.HiddenInput()

        # wedding_date 필드에 DateTimeInput 위젯 사용
        self.fields['wedding_date'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})