import os

import environ
import requests
from django.shortcuts import render, redirect

from wedding_card.settings import BASE_DIR

environ.Env.read_env(env_file=os.path.join(BASE_DIR, '.env'))
env = environ.Env(DEBUG=(bool, False))
CLIENT_ID = env('client_id')
CLIENT_SECRET = env('client_secret')


def hello_world(request):
    return render(request, 'account/hello_world.html')


def login(request):
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
    return redirect('/accounts/test/')


def sign_up(request):
    return render(request, 'account/signup.html')

