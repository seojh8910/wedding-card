from django.urls import path

from card import views

app_name = 'card'

urlpatterns = [
    path('list/', views.list_card, name='list'),
    path('create/', views.create_card, name='create'),
    path('detail/<int:pk>/', views.detail_card, name='detail'),
    path('update/<int:pk>/', views.update_card, name='update'),
    path('delete/<int:pk>/', views.delete_card, name='delete'),
]