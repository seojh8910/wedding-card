from django.urls import path

from account import views

app_name = 'account'

urlpatterns = [
    path('test/', views.hello_world, name='hello_world'),
    path('login/', views.login, name='login'),
    path('signup/', views.sign_up, name='sign_up'),
]