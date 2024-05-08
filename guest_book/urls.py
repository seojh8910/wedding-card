from django.urls import path

from guest_book import views

app_name = 'guestbook'

urlpatterns = [
    path('create/', views.guestbook_create, name='create'),
    path('delete/<int:pk>/', views.guestbook_delete, name='delete'),
]
