from django.db import models
from django.contrib.auth.models import User

#from users.models import User

class Shop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='media/shop_logos/%Y/%m/%d', blank=True, null=True) 
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='shop', null=True, blank=True)
    delivery_person = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_shops')
    maintenance_services = models.TextField(blank=True)  # عرض فقط

    def __str__(self):
        return self.name
    
    
    class Meta:
        db_table = "shop"  # اسم الجدول النهائي في قاعدة البيانات

