import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_site.settings')
import django
django.setup()
from pages.models import Item, Rental, Notification
from pages.views import rental_request_view
from django.test.client import RequestFactory
from django.contrib.auth import get_user_model

User = get_user_model()
# Create test users and item if not exist
borrower, _ = User.objects.get_or_create(username='test_borrower')
borrower.set_password('testpass')
borrower.hostel_name='H'
borrower.room_number='101'
borrower.phone_number='000'
borrower.save()

owner, _ = User.objects.get_or_create(username='test_owner')
owner.set_password('testpass')
owner.hostel_name='H'
owner.room_number='102'
owner.phone_number='111'
owner.save()

item, created = Item.objects.get_or_create(name='Test Item', owner=owner, defaults={'description':'desc','price':'10.00'})

rf = RequestFactory()
request = rf.get(f'/item/{item.pk}/rent/')
request.user = borrower

response = rental_request_view(request, pk=item.pk)
print('GET response status:', getattr(response, 'status_code', 'no status'))

# Now try POST
request = rf.post(f'/item/{item.pk}/rent/', data={'start_date':'2025-10-10','end_date':'2025-10-12','notes':'Please'})
# Need messages storage
from django.contrib.messages.storage.fallback import FallbackStorage
request.user = borrower
request._messages = FallbackStorage(request)

response = rental_request_view(request, pk=item.pk)
print('POST response (should be redirect):', getattr(response, 'status_code', 'no status'))
print('Rentals for borrower:', list(Rental.objects.filter(borrower=borrower)))
print('Notifications for owner:', list(Notification.objects.filter(user=owner)))
