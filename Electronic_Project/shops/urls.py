from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                   # الصفحة الرئيسية
    path('shops_list/', views.shop_list, name='shop_list'),   # قائمة المحلات
    path('shops/<int:pk>/', views.shop_detail, name='shop_detail'),  # تفاصيل محل
    path('shops/add/', views.shop_create, name='shop_create'),       # إضافة محل
    path('shops/<int:pk>/edit/', views.shop_update, name='shop_update'), # تعديل محل
    path('shops/<int:pk>/delete/', views.shop_delete, name='shop_delete'), # حذف محل
]
