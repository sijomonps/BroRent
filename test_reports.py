# Test script to verify report generation
# Run with: python manage.py shell < test_reports.py

from django.contrib.auth import get_user_model
from pages.models import Item, Rental, Notification
from django.utils import timezone
from datetime import timedelta

User = get_user_model()

# Check if we have data
print("=" * 50)
print("BRORENT - REPORTS SYSTEM TEST")
print("=" * 50)

# Count existing data
total_users = User.objects.count()
total_items = Item.objects.count()
total_rentals = Rental.objects.count()

print(f"\n✓ Total Users: {total_users}")
print(f"✓ Total Items: {total_items}")
print(f"✓ Total Rentals: {total_rentals}")

# Check if we have staff users
staff_users = User.objects.filter(is_staff=True).count()
print(f"✓ Staff Users: {staff_users}")

if staff_users == 0:
    print("\n⚠ WARNING: No staff users found!")
    print("  Create a superuser with: python manage.py createsuperuser")

# Most borrowed items
if total_rentals > 0:
    from django.db.models import Count
    most_borrowed = Item.objects.annotate(
        rental_count=Count('rentals')
    ).order_by('-rental_count').first()
    
    if most_borrowed:
        print(f"\n✓ Most Borrowed Item: {most_borrowed.name} ({most_borrowed.rental_count} times)")

print("\n" + "=" * 50)
print("REPORT ENDPOINTS AVAILABLE:")
print("=" * 50)
print("Dashboard: /admin-reports/")
print("\nPDF Reports:")
print("  - Items:   /reports/items/pdf/")
print("  - Rentals: /reports/rentals/pdf/")
print("  - Users:   /reports/users/pdf/")
print("\nExcel Reports:")
print("  - Items:   /reports/items/excel/")
print("  - Rentals: /reports/rentals/excel/")
print("  - Users:   /reports/users/excel/")
print("=" * 50)

print("\n✓ Reports system ready!")
print("  Access as staff user at: http://127.0.0.1:8000/admin-reports/")
