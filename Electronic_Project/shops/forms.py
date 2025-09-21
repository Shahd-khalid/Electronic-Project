from django import forms
from .models import Shop

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'address', 'logo','maintenance_services']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
          #  'owner': forms.TextInput(attrs={'class': 'form-control'}),    
            'logo': forms.FileInput(attrs={'class': 'form-control'}),
            #'delivery_person': forms.TextInput(attrs={'class': 'form-control'}),
            'maintenance_services': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }