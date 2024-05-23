from django.urls import path

from account import views

app_name = 'account'

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('google/login/', views.google_login, name='google_login'),
    path('google/login/callback/', views.google_login_callback, name='google_callback'),
    path('signup/', views.sign_up, name='sign_up'),
]