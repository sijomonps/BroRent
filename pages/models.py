
from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom user model
class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='user_images/', blank=True, null=True)
    hostel_name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.username

# Make sure this whole class is in your pages/models.py file
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    owner = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    per_day = models.BooleanField(default=False, help_text='Is this price per day?')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
