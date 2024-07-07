from django import forms
from django.forms import DateTimeInput, inlineformset_factory

from card.models import Card, Transport, Account


class CardCreationForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'
        exclude = ('user', 'guests_comment',)
        widgets = {
            'theme': forms.Select(attrs={'class': 'inorder_txt'}),
            'wedding_date': forms.DateTimeInput(attrs={'class': 'inorder_txt', 'type': 'datetime-local', 'style': 'width: calc(100% - 22px); max-width: 180px;'}),
            'main_img': forms.ClearableFileInput(attrs={'onchange': 'previewImage(event)', 'style': 'display:none;', 'data-preview':'preview1', 'class': 'image-input'}),
            'wedding_hall_name': forms.TextInput(attrs={'class': 'inorder_txt', 'style': 'width: calc(100% - 20px); max-width: 378px;'}),
            'wedding_hall_floor': forms.TextInput(attrs={'class': 'inorder_txt', 'style': 'width: calc(100% - 20px); max-width: 378px;'}),
            'wedding_hall_address': forms.TextInput(attrs={'id': 'address', 'class': 'inorder_txt', 'style': 'width: calc(100% - 87px);', 'onclick': 'address_search()'}),

            'invitation_title': forms.TextInput(attrs={'class': 'inorder_txt', 'placeholder': '초대합니다', 'style': 'width: calc(100% - 22px);'}),
            'invitation_content': forms.Textarea(attrs={'class': 'te-textarea', 'placeholder': '살랑이는 바람결에\n사랑이 묻어나는 계절입니다.\n여기 곱고 예쁜 두 사람이 사랑을 맺어\n인생의 반려자가 되려 합니다.\n새 인생을 시작하는 이 자리에 오셔서\n축복해 주시면 감사하겠습니다.',
                                                        'contenteditable': 'true', 'style': 'height: 120px; text-align: center;', 'onkeydown': 'enterkeydown()'}),

            'groom_name': forms.TextInput(attrs={'class': 'inorder_txt', 'placeholder': '성함', 'style': 'width: calc(100% - 22px); max-width: 150px;'}),
            'groom_mother_name': forms.TextInput(attrs={'class': 'inorder_txt', 'placeholder': '성함', 'style': 'width: calc(100% - 22px); max-width: 150px;'}),
            'groom_father_name': forms.TextInput(attrs={'class': 'inorder_txt', 'placeholder': '성함', 'style': 'width: calc(100% - 22px); max-width: 150px;'}),
            'groom_position': forms.Select(attrs={'class': 'inorder_txt'}),

            'bride_name': forms.TextInput(attrs={'class': 'inorder_txt', 'placeholder': '성함', 'style': 'width: calc(100% - 22px); max-width: 150px;'}),
            'bride_mother_name': forms.TextInput(attrs={'class': 'inorder_txt', 'placeholder': '성함', 'style': 'width: calc(100% - 22px); max-width: 150px;'}),
            'bride_father_name': forms.TextInput(attrs={'class': 'inorder_txt', 'placeholder': '성함', 'style': 'width: calc(100% - 22px); max-width: 150px;'}),
            'bride_position': forms.Select(attrs={'class': 'inorder_txt'}),

            'contact_groom_title_1': forms.TextInput(attrs={'class': 'inorder_txt black', 'placeholder': '신랑', 'style': 'width: 80px;'}),
            'contact_groom_name_1': forms.TextInput(attrs={'class': 'inorder_txt black', 'placeholder': '성함', 'style': 'width: 60px;'}),
            'contact_groom_phone_number_1': forms.TextInput(attrs={'class': 'inorder_txt', 'placeholder': '전화번호', 'type': 'tel', 'style': 'width: 100px;'}),

            'contact_groom_title_2': forms.TextInput(attrs={'class': 'inorder_txt black', 'placeholder': '신랑 아버지', 'style': 'width: 80px;'}),
            'contact_groom_name_2': forms.TextInput(attrs={'class': 'inorder_txt black', 'placeholder': '성함', 'style': 'width: 60px;'}),
            'contact_groom_phone_number_2': forms.TextInput(attrs={'class': 'inorder_txt', 'placeholder': '전화번호', 'type': 'tel', 'style': 'width: 100px;'}),

            'contact_groom_title_3': forms.TextInput(attrs={'class': 'inorder_txt black', 'placeholder': '신랑 어머니', 'style': 'width: 80px;'}),
            'contact_groom_name_3': forms.TextInput(attrs={'class': 'inorder_txt black', 'placeholder': '성함', 'style': 'width: 60px;'}),
            'contact_groom_phone_number_3': forms.TextInput(attrs={'class': 'inorder_txt', 'placeholder': '전화번호', 'type': 'tel', 'style': 'width: 100px;'}),

            'contact_bride_title_1': forms.TextInput(attrs={'class': 'inorder_txt black', 'placeholder': '신부', 'style': 'width: 80px;'}),
            'contact_bride_name_1': forms.TextInput(attrs={'class': 'inorder_txt black', 'placeholder': '성함', 'style': 'width: 60px;'}),
            'contact_bride_phone_number_1': forms.TextInput(attrs={'class': 'inorder_txt', 'placeholder': '전화번호', 'type': 'tel', 'style': 'width: 100px;'}),

            'contact_bride_title_2': forms.TextInput(attrs={'class': 'inorder_txt black', 'placeholder': '신부 아버지', 'style': 'width: 80px;'}),
            'contact_bride_name_2': forms.TextInput(attrs={'class': 'inorder_txt black', 'placeholder': '성함', 'style': 'width: 60px;'}),
            'contact_bride_phone_number_2': forms.TextInput(attrs={'class': 'inorder_txt', 'placeholder': '전화번호', 'type': 'tel','style': 'width: 100px;'}),

            'contact_bride_title_3': forms.TextInput(attrs={'class': 'inorder_txt black', 'placeholder': '신부 어머니', 'style': 'width: 80px;'}),
            'contact_bride_name_3': forms.TextInput(attrs={'class': 'inorder_txt black', 'placeholder': '성함', 'style': 'width: 60px;'}),
            'contact_bride_phone_number_3': forms.TextInput(attrs={'class': 'inorder_txt', 'placeholder': '전화번호', 'type': 'tel','style': 'width: 100px;'}),

            'thumb_img': forms.ClearableFileInput(attrs={'onchange': 'previewImage(event)', 'style': 'display:none;', 'data-preview': 'preview2', 'class': 'image-input'}),
            'thumb_title': forms.TextInput(attrs={'class': 'inorder_txt', 'placeholder': '김신랑♥이신부 결혼합니다', 'style': 'max-width: 260px; width: calc(100% - 22px);'}),
            'thumb_content': forms.Textarea(attrs={'class': 'inorder_txt', 'placeholder': '5월 30일 목요일 오후 1시 30분', 'style': 'width: calc(100% - 22px); max-width: 260px; height: 80px;'}),
        }
        labels = {
            'theme': '테마',
            'wedding_date': '결혼식 날짜',
            'wedding_hall_name': '예식장명',
            'wedding_hall_floor': '층과 홀',
            'wedding_hall_address': '예식장 주소',
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


class TransportForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'inorder_txt', 'style': 'width: calc(100% - 22px);', 'placeholder': '버스, 지하철, 자가용 등'}),
            'description': forms.Textarea(attrs={'class': 'te-textarea', 'style': 'height: 100px;'}),
        }


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['group', 'holder', 'bank', 'number']
        widgets = {
            'group': forms.TextInput(attrs={'class': 'inorder_txt', 'style': 'width: calc(100% - 22px);'}),
            'bank': forms.TextInput(attrs={'class': 'inorder_txt', 'placeholder': '은행', 'style': 'width: calc(100% - 27px);'}),
            'number': forms.TextInput(attrs={'class': 'inorder_txt', 'placeholder': '계좌번호', 'style': 'width: calc(100% - 22px);'}),
            'holder': forms.TextInput(attrs={'class': 'inorder_txt', 'style': 'width: calc(100% - 22px);'}),
        }


TransportFormSet = inlineformset_factory(Card, Transport, form=TransportForm, extra=1)
AccountFormSet = inlineformset_factory(Card, Account, form=AccountForm, extra=1)
