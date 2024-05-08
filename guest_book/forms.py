from django import forms

from guest_book.models import GuestBook


class GuestBookCreationForm(forms.ModelForm):
    password = forms.CharField(
        label='비밀번호',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'})
    )

    class Meta:
        model = GuestBook
        fields = ['writer', 'password', 'content']
        labels = {
            'writer': '작성자',
            'content': '방명록',
        }
