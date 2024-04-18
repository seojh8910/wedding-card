from django.urls import path
from account.views import hello_world

app_name = 'account'

urlpatterns = [
    path('test/', hello_world, name='hello_world')
]