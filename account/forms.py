from django.contrib.auth.forms import UserCreationForm

from account.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone_number']
        error_messages = {
            'password_mismatch': ('비밀번호 확인이 맞지 않습니다.'),
        }