from django.contrib.auth.forms import UserCreationForm
from django import forms

from account.models import User


class CreateUserForm(UserCreationForm):
    type = forms.CharField(widget=forms.HiddenInput(),initial='basic')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone_number', 'type']
        error_messages = {
            'password_mismatch': ('비밀번호 확인이 맞지 않습니다.'),
        }

class LoginForm(forms.Form):
    email = forms.CharField(max_length=100, required=True, widget=forms.TextInput())
    password = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput())