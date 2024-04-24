from django.urls import path

from board import views

app_name = 'board'

urlpatterns = [
    path('list/', views.board_list, name='board_list'),
    path('create/', views.board_create, name='board_create'),
]