from django.urls import path

from payment import views

app_name = 'payment'

urlpatterns = [
    path('save/', views.save_payment, name='save'),
]