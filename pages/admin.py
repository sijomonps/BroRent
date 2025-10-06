from django.contrib import admin

# pages/admin.py

from django.contrib import admin
from .models import Item  # 1. Import your Item model

# Register your models here.
admin.site.register(Item)  # 2. Register the Item model with the admin site
