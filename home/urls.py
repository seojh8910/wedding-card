from django.urls import path

from home import views

app_name = 'home'

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
]
