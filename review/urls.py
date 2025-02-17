from django.urls import path

from review import views

app_name = 'review'

urlpatterns = [
    path('list/', views.review_list, name='review_list'),
    path('create/', views.review_create, name='review_create'),
    path('delete/<int:pk>', views.review_delete, name='review_delete'),
]