from django.contrib.auth.forms import UserCreationForm
from django import forms

from account.models import User


class CreateUserForm(UserCreationForm):
    type = forms.CharField(widget=forms.HiddenInput(), initial='basic', required=False)
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
        error_messages={
            'required': '비밀번호를 입력해주세요.',
        }
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput,
        strip=False,
        error_messages={
            'required': '비밀번호 확인을 입력해주세요.',
            'password_mismatch': '비밀번호 확인이 맞지 않습니다.',
        }
    )

    class Meta:
        model = User
        fields = '__all__'
        exclude = ('username', 'type', 'date_joined', 'password', )
        error_messages = {
            'email': {
                'required': '이메일을 입력해주세요.',
                'unique': '이미 사용 중인 이메일입니다.'
            },
            'phone_number': {
                'required': '전화번호를 입력해주세요.'
            }
        }


class LoginForm(forms.Form):
    email = forms.CharField(max_length=100, required=True, widget=forms.TextInput(),
                            error_messages={'required': '이메일을 입력해주세요.', })
    password = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(),
                               error_messages={'required': '비밀번호를 입력해주세요.', })


class CreateSocialUserForm(UserCreationForm):
    type = forms.CharField(widget=forms.HiddenInput(), initial='basic')
    password1 = forms.CharField(
        widget=forms.HiddenInput(),
        initial='defaultpassword',
        required=False
    )
    password2 = forms.CharField(
        widget=forms.HiddenInput(),
        initial='defaultpassword',
        required=False
    )

    class Meta:
        model = User
        fields = ['username', 'email',  'phone_number', 'type']

    def save(self, commit=True):
        user = super(CreateSocialUserForm, self).save(commit=False)
        user.set_unusable_password()
        if commit:
            user.save()
        return user
