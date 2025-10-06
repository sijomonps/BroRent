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

class ItemSearchForm(forms.Form):
    SORT_CHOICES = [
        ('price_asc', 'Price (Low to High)'),
        ('price_desc', 'Price (High to Low)'),
        ('date_desc', 'Newest First'),
        ('date_asc', 'Oldest First'),
    ]
    
    search = forms.CharField(required=False, label='Search',
                           widget=forms.TextInput(attrs={'placeholder': 'Search items...'}))
    category = forms.ChoiceField(choices=[('', 'All Categories')] + Item.CATEGORY_CHOICES,
                               required=False)
    availability = forms.BooleanField(required=False, initial=True)
    sort_by = forms.ChoiceField(choices=SORT_CHOICES, required=False,
                              initial='date_desc')

class ItemForm(forms.ModelForm):
    category = forms.ChoiceField(
        choices=Item.CATEGORY_CHOICES,
        required=True,
        widget=forms.Select(attrs={
            'class': 'rounded-md border-gray-300 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50',
            'placeholder': 'Select a category'
        })
    )

    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'image', 'category', 'is_available', 'per_day']
        labels = {
            'name': 'Item Name',
            'description': 'Item Description',
            'price': 'Price',
            'image': 'Item Image',
            'category': 'Category',
            'is_available': 'Is Available',
            'per_day': 'Price is per day'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'rounded-md border-gray-300 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50',
                'placeholder': 'Enter item name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'rounded-md border-gray-300 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50',
                'rows': 4,
                'placeholder': 'Enter item description'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'rounded-md border-gray-300 shadow-sm focus:border-blue-300 focus:ring focus:ring-blue-200 focus:ring-opacity-50',
                'placeholder': 'Enter price'
            })
        }