import os
import environ
import requests
from django.contrib.auth import login, logout

from django.shortcuts import render, redirect
from django.contrib import messages
from account.forms import CreateUserForm, LoginForm, CreateSocialUserForm
from account.models import User

from wedding_card.settings import BASE_DIR

environ.Env.read_env(env_file=os.path.join(BASE_DIR, '.env'))
env = environ.Env(DEBUG=(bool, False))
CLIENT_ID = env('client_id')
CLIENT_SECRET = env('client_secret')


def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password")
            try:
                user = User.objects.get(email=email)
                if user.check_password(raw_password):
                    login(request, user)
                    return redirect('home:landing_page')
                else:
                    messages.error(request, "비밀번호가 일치하지 않습니다.")
                    return render(request, 'account/login.html', {"form": form})
            except User.DoesNotExist:
                messages.error(request, "아이디와 비밀번호를 확인해주세요.")
                return render(request, 'account/login.html', {"form": form})
        else:
            messages.error(request, "아이디와 비밀번호를 확인해주세요.")
            return render(request, 'account/login.html', {"form": form})
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {"form": form})


def logout_page(request):
    next_path = request.GET.get('next', '/accounts/test/')
    logout(request)
    return redirect(next_path)


def google_login(request):
    google_auth_api = "https://accounts.google.com/o/oauth2/v2/auth"
    scope = "https://www.googleapis.com/auth/userinfo.email " + \
            "https://www.googleapis.com/auth/userinfo.profile"
    redirect_uri = f'http://{request.META.get("HTTP_HOST")}/accounts/google/login/callback/'

    return redirect(f"{google_auth_api}?client_id={CLIENT_ID}&response_type=code&redirect_uri={redirect_uri}&scope={scope}")


def google_login_callback(request):
    code = request.GET.get('code')
    redirect_uri = f'http://{request.META.get("HTTP_HOST")}/accounts/google/login/callback/'
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
        return render(request, 'account/signup.html', context={'email': user_email, 'type': 'gmail'})
    login(request, user)
    return redirect('home:landing_page')


def sign_up(request):
    if request.method == 'POST':
        if request.POST.get('type') == 'basic':
            form = CreateUserForm(request.POST)
        else:
            form = CreateSocialUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'새로운 계정이 생성되었습니다.: {username}')
            login(request, user)
            messages.info(request, f"{username}으로 로그인 되었습니다.")
            return redirect('home:landing_page')
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
                else:
                    messages.error(request, "뭔가 오류!!!!!")
            return render(request=request, template_name='account/signup.html', context={'form': form})
    return render(request, 'account/signup.html', context={'type': 'basic'})

