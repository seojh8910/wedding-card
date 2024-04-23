import os
import environ
import requests
from django.contrib.auth import login

from django.shortcuts import render, redirect
from django.contrib import messages
from account.forms import CreateUserForm
from account.models import User

from wedding_card.settings import BASE_DIR

environ.Env.read_env(env_file=os.path.join(BASE_DIR, '.env'))
env = environ.Env(DEBUG=(bool, False))
CLIENT_ID = env('client_id')
CLIENT_SECRET = env('client_secret')


def hello_world(request):
    return render(request, 'account/hello_world.html')


def login_page(request):
    return render(request, 'account/login.html')


def google_login(request):
    google_auth_api = "https://accounts.google.com/o/oauth2/v2/auth"
    scope = "https://www.googleapis.com/auth/userinfo.email " + \
            "https://www.googleapis.com/auth/userinfo.profile"
    redirect_uri = 'http://127.0.0.1:8000/accounts/google/login/callback/'

    return redirect(f"{google_auth_api}?client_id={CLIENT_ID}&response_type=code&redirect_uri={redirect_uri}&scope={scope}")


def google_login_callback(request):
    code = request.GET.get('code')
    redirect_uri = 'http://127.0.0.1:8000/accounts/google/login/callback/'
    if not code:
        return 'code does not exists'
    token_req = requests.post(
        f"https://oauth2.googleapis.com/token?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&code={code}&grant_type=authorization_code&redirect_uri={redirect_uri}")
    access_token = token_req.json().get('access_token')
    user_info_response = requests.get("https://www.googleapis.com/oauth2/v3/userinfo", params={'access_token': access_token})
    user_info = user_info_response.json()
    user_email = user_info.get('email')
    if not user_email:
        return 'user email does not exists'
    user = User.objects.filter(email=user_email).first()
    if not user:
        create_data = {'email': user_email, 'type': 'gmail'}
        form = CreateUserForm(initial=create_data)
        return render(request, 'account/signup.html', context={'form': form})
    login(request, user)
    return redirect('/accounts/test/')


def sign_up(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'새로운 계정이 생성되었습니다.: {username}')
            login(request, user)
            messages.info(request, f"{username}으로 로그인 되었습니다.")
            return redirect('account:hello_world')
        else:
            password1 = form.data['password1']
            password2 = form.data['password2']
            for msg in form.errors.as_data():
                if msg == 'email':
                    messages.error(request, "유효하지 않은 이메일입니다.")
                if msg == 'password2' and password1 == password2:
                    messages.error(request, "복잡한 비밀번호가 필요합니다.")
                elif msg == 'password2' and password1 != password2:
                    messages.error(request, "비밀번호가 일치하지 않습니다.")
            return render(request=request, template_name='account/signup.html', context={'form': form})
    form = CreateUserForm
    return render(request, 'account/signup.html', context={'form': form})

