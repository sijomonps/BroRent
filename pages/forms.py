# pages/forms.py
from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Item

class CustomUserCreationForm(UserCreationForm):
    image = forms.ImageField(required=False)
    hostel_name = forms.CharField(max_length=100)
    room_number = forms.CharField(max_length=20)
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = CustomUser
        fields = ('username', 'image', 'hostel_name', 'room_number', 'phone_number', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'image', 'is_available', 'per_day']