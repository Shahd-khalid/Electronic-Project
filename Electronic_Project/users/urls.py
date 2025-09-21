# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('create/', views.user_create, name='user_create'),
    # لاحقًا يمكن إضافة user_list, user_update, user_delete
]
