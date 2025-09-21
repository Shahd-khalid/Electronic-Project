# users/forms.py
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    again_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'again_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        again_password = cleaned_data.get("again_password")

        if password and again_password and password != again_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data
