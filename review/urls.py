from django.urls import path

from review import views

app_name = 'review'

urlpatterns = [
    path('list/', views.review_list, name='review_list'),
]