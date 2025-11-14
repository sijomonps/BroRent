# pages/forms.py
from django import forms
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Item, Rental

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

class UserProfileEditForm(forms.ModelForm):
    """Form for editing user profile information"""
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'image', 'hostel_name', 'room_number', 'phone_number']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition',
                'placeholder': 'Your username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition',
                'placeholder': 'your.email@example.com'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition',
                'placeholder': 'First name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition',
                'placeholder': 'Last name'
            }),
            'hostel_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition',
                'placeholder': 'Hostel name'
            }),
            'room_number': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition',
                'placeholder': 'Room number'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition',
                'placeholder': 'Phone number'
            })
        }
        labels = {
            'username': 'Username',
            'email': 'Email Address',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image': 'Profile Picture',
            'hostel_name': 'Hostel Name',
            'room_number': 'Room Number',
            'phone_number': 'Phone Number'
        }

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

class RentalRequestForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['start_date', 'end_date', 'notes']
        widgets = {
            'start_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'
            }),
            'end_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'
            }),
            'notes': forms.Textarea(attrs={
                'rows': 3,
                'class': 'rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50',
                'placeholder': 'Any special requests or notes for the lender?'
            })
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date:
            if start_date < timezone.now().date():
                raise forms.ValidationError("Start date cannot be in the past.")
            if end_date < start_date:
                raise forms.ValidationError("End date must be after start date.")

        return cleaned_data

class ItemForm(forms.ModelForm):
    category = forms.ChoiceField(
        choices=Item.CATEGORY_CHOICES,
        required=True,
        widget=forms.Select(attrs={
            'class': 'rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50',
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