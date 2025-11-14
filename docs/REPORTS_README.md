# BroRent - Admin Reports & Export System

## Overview
The BroRent platform now includes a comprehensive admin reporting system that allows staff members to generate and export detailed reports for academic evaluation and project documentation.

## Features

### 📊 Reports Dashboard
- **Summary Statistics**: View total items, users, rentals, active rentals, and pending requests at a glance
- **Most Borrowed Items**: See top 10 most popular items with rental counts
- **Top Borrowers**: Track most active users borrowing items
- **Top Lenders**: Identify users lending most frequently

### 📄 PDF Reports
Generate professional PDF reports with:
- **Items Report**: Complete list of all items with owner, category, price, and availability
- **Rental Activity Report**: Most borrowed items ranked with rental statistics
- **User Activity Report**: Top borrowers and lenders with contact information

### 📊 Excel Reports
Export detailed data to Excel (.xlsx) for further analysis:
- **Items Report**: Full item database with descriptions and dates
- **Rental Activity Report**: 
  - Sheet 1: All rental transactions with dates and prices
  - Sheet 2: Most borrowed items with revenue analysis
- **User Activity Report**: Complete user database with activity metrics

## Access Requirements

### For Staff/Admin Users
1. User must have `is_staff=True` flag enabled
2. Access the dashboard at: `/admin-reports/`
3. Reports link appears automatically in the navbar for staff users

### Creating a Staff User
```bash
# Create superuser (has staff privileges)
python manage.py createsuperuser

# Or promote existing user via Django shell:
python manage.py shell
>>> from django.contrib.auth import get_user_model
>>> User = get_user_model()
>>> user = User.objects.get(username='your_username')
>>> user.is_staff = True
>>> user.save()
```

## URLs

### Dashboard
- `/admin-reports/` - Main reports dashboard

### PDF Exports
- `/reports/items/pdf/` - Items report
- `/reports/rentals/pdf/` - Rentals report
- `/reports/users/pdf/` - Users activity report

### Excel Exports
- `/reports/items/excel/` - Items report
- `/reports/rentals/excel/` - Rentals report
- `/reports/users/excel/` - Users activity report

## Report Contents

### 1. Items Report
**Includes:**
- Item ID, Name, Description
- Owner information
- Category classification
- Price and per-day flag
- Availability status
- Date posted

**Use Cases:**
- Inventory management
- Category distribution analysis
- Pricing analysis
- Owner activity tracking

### 2. Rental Activity Report
**Includes:**
- All rental transactions
- Item names and categories
- Borrower and lender details
- Rental dates and duration
- Status (pending, approved, borrowed, returned)
- Total price calculations
- Most borrowed items ranking

**Use Cases:**
- Revenue tracking
- Popular item identification
- Rental duration analysis
- Status tracking

### 3. User Activity Report
**Includes:**
- User ID, Username
- Contact information (hostel, room, phone)
- Items listed count
- Times borrowed count
- Times lent count
- Date joined
- Top performers ranking

**Use Cases:**
- User engagement analysis
- Active user identification
- Platform usage statistics
- Community participation tracking

## Technical Implementation

### Dependencies
```bash
pip install reportlab  # PDF generation
pip install openpyxl   # Excel generation
```

### Key Features
- **Professional PDF formatting** with ReportLab
  - Custom headers and styling
  - Tables with proper formatting
  - Summary statistics
  
- **Structured Excel exports** with OpenPyXL
  - Multiple sheets for complex reports
  - Styled headers
  - Auto-adjusted column widths
  
- **Security**
  - `@staff_member_required` decorator on all views
  - Automatic permission checking
  
- **Performance**
  - Efficient database queries with annotations
  - Optimized for large datasets

## For Academic Evaluation

These reports are specifically designed for:
- **Project Documentation**: Comprehensive data exports
- **Academic Presentations**: Professional PDF reports
- **Data Analysis**: Excel format for further processing
- **System Metrics**: Usage statistics and trends
- **Evaluation Evidence**: Real platform data for assessment

## Troubleshooting

### "Permission Denied" Error
- Ensure user has `is_staff=True` flag
- Log in with staff/superuser credentials

### Empty Reports
- Add sample data to database
- Create items, rentals, and users for testing

### PDF/Excel Download Issues
- Check file download settings in browser
- Verify reportlab and openpyxl are installed

## Future Enhancements
- Date range filtering
- Category-specific reports
- Revenue analytics dashboard
- Email report scheduling
- Custom report builder

## Usage Example

1. **Login** as staff user
2. **Navigate** to Reports (navbar link)
3. **View** dashboard statistics
4. **Click** PDF or Excel button for desired report
5. **Download** automatically starts
6. **Open** with PDF viewer or Excel

## Support
For issues or questions about the reporting system, contact the development team or create an issue in the repository.
