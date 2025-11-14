
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
    CATEGORY_CHOICES = [
        ('clothes', 'Clothes'),
        ('accessories', 'Accessories'),
        ('gadgets', 'Gadgets'),
        ('books', 'Books'),
        ('sports', 'Sports Equipment'),
        ('others', 'Others'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    owner = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    per_day = models.BooleanField(default=False, help_text='Is this price per day?')
    date_posted = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='others')

    def __str__(self):
        return self.name
    
    def is_currently_rented(self):
        """Check if item is currently rented based on active rental dates"""
        from datetime import date
        today = date.today()
        
        # Check for active rentals (approved or borrowed status) that overlap with today
        active_rentals = self.rentals.filter(
            status__in=['approved', 'borrowed'],
            start_date__lte=today,
            end_date__gte=today
        )
        
        return active_rentals.exists()
    
    def get_availability_status(self):
        """Get the real-time availability status"""
        if not self.is_available:
            return False
        return not self.is_currently_rented()

class Rental(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
        ('rejected', 'Rejected'),
        ('cancelled', 'Cancelled'),
    ]

    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='rentals')
    borrower = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='borrowed_items')
    lender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='lent_items')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    request_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(help_text='When do you want to borrow the item?')
    end_date = models.DateField(help_text='When will you return the item?')
    approved_date = models.DateTimeField(null=True, blank=True)
    borrowed_date = models.DateTimeField(null=True, blank=True)
    returned_date = models.DateTimeField(null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    notes = models.TextField(blank=True, help_text='Any special requests or notes?')

    def __str__(self):
        return f"{self.borrower.username} - {self.item.name} ({self.status})"

    def save(self, *args, **kwargs):
        # Calculate total price if per_day is True
        if self.item.per_day and self.start_date and self.end_date:
            days = (self.end_date - self.start_date).days + 1
            self.total_price = self.item.price * days
        else:
            self.total_price = self.item.price
        super().save(*args, **kwargs)

class Notification(models.Model):
    TYPE_CHOICES = [
        ('rental_request', 'New Rental Request'),
        ('request_approved', 'Request Approved'),
        ('request_rejected', 'Request Rejected'),
        ('item_borrowed', 'Item Borrowed'),
        ('item_returned', 'Item Returned'),
        ('reminder', 'Return Reminder'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notifications')
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE, related_name='notifications')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.type} ({self.created_at})"

