from django.urls import path

from board import views

app_name = 'board'

urlpatterns = [
    path('list/', views.board_list, name='board_list'),
    path('create/', views.board_create, name='board_create'),
    path('delete/<int:pk>', views.board_delete, name='board_delete'),
    path('detail/<int:pk>', views.board_detail, name='board_detail'),
    path('update/<int:pk>', views.board_update, name='board_update'),
]