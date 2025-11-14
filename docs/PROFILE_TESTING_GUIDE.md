# Profile Features - Visual Testing Guide

## 🧪 Quick Test Checklist

### Server Status
✅ **Server running at:** http://127.0.0.1:8000/  
✅ **System check:** 0 issues  
✅ **Recent successful requests:**
- `/profile/` - 200 OK
- `/my-rented-items/` - 200 OK  
- `/my-lended-items/` - 200 OK
- Media files serving correctly

---

## 📍 Testing Routes

### 1. Profile Page
**URL:** http://127.0.0.1:8000/profile/

**What to Check:**
- [ ] Profile picture or gradient avatar displays
- [ ] Username and contact info visible
- [ ] 4 statistics cards show correct numbers
- [ ] "Items Listed", "Items Borrowed", "Items Lent", "Active Rentals"
- [ ] Quick action links work (Change Password, My Rented Items, My Lended Items)
- [ ] Your listed items appear in grid
- [ ] Edit and Delete buttons on your items
- [ ] "List New Item" button at bottom

**Visual Features:**
- Gradient background cards (purple, blue, green, pink)
- Circular profile image with border
- Responsive grid layout
- Hover effects on buttons

---

### 2. Password Change
**URL:** http://127.0.0.1:8000/password-change/

**What to Check:**
- [ ] Three input fields: Old, New, Confirm password
- [ ] Password requirements list displays
- [ ] Form submits successfully
- [ ] Success message appears
- [ ] Redirects to profile page
- [ ] User stays logged in (not logged out)
- [ ] Can log in with new password

**Requirements Shown:**
- Minimum 8 characters
- Not entirely numeric
- Not too similar to username
- Not commonly used password

---

### 3. My Rented Items
**URL:** http://127.0.0.1:8000/my-rented-items/

**What to Check:**
- [ ] **Active Rentals** section (green header)
  - Shows items with status='borrowed'
  - Item image, name, price
  - Start and end dates
  - Owner contact info
  
- [ ] **Approved Requests** section (blue header)
  - Shows items with status='approved'
  - Waiting to be picked up
  
- [ ] **Pending Requests** section (yellow header)
  - Shows items with status='pending'
  - Awaiting owner approval
  
- [ ] **Completed Rentals** section (gray header)
  - Shows items with status='returned'
  - Historical records
  
- [ ] **Rejected Requests** section (red header)
  - Shows items with status='rejected'
  - Declined by owner

**Visual Features:**
- Color-coded section headers
- Status badges on cards
- Empty state messages if no items
- "View Item Details" buttons

---

### 4. My Lended Items
**URL:** http://127.0.0.1:8000/my-lended-items/

**What to Check:**
- [ ] **Pending Requests** section (yellow header)
  - Shows rental requests for your items
  - Borrower profile picture/avatar
  - Borrower username and contact info
  - Requested dates and notes
  - **Accept Request** button (green)
  - **Reject Request** button (red)
  
- [ ] **Active Lendings** section (green header)
  - Items currently borrowed
  - Borrower contact information
  - Return date tracking
  
- [ ] **Completed Lendings** section (gray header)
  - Historical lending records
  - Past borrowers and dates

**Action Testing:**
1. Click "Accept Request":
   - Changes status to 'approved'
   - Shows success message
   - Request moves from pending to active
   - Notification sent to borrower

2. Click "Reject Request":
   - Changes status to 'rejected'
   - Shows success message
   - Request removed from pending
   - Notification sent to borrower

---

## 🖼️ User Image Display Testing

### Navbar (Top-Right)
**Where:** Every page when logged in

**Check:**
- [ ] Profile picture appears in circular frame
- [ ] If no image: gradient avatar with first letter
- [ ] Border color: indigo-200
- [ ] Hover effect: border-indigo-400
- [ ] Size: 40x40 pixels (w-10 h-10)
- [ ] Links to profile page

**Test:**
1. Log in with user who has profile picture
2. Check navbar top-right corner
3. Should see circular image or gradient avatar

---

### Item Detail Page
**Where:** http://127.0.0.1:8000/item/{id}/

**Check:**
- [ ] Owner information card displays
- [ ] Owner profile picture (64x64 pixels)
- [ ] If no image: gradient avatar with initial
- [ ] Owner username, phone, hostel, room shown
- [ ] Card has gradient background (gray-50 to gray-100)
- [ ] Border around card

**Test:**
1. Click any item to view details
2. Scroll to owner information section
3. Should see owner's profile picture and contact info

---

### Item List/Home Page
**Where:** http://127.0.0.1:8000/home/

**Check:**
- [ ] Small owner avatar on each item card (24x24 pixels)
- [ ] "by [username]" text next to avatar
- [ ] Gradient fallback if no image
- [ ] Located above price/date section

**Test:**
1. Go to home page or browse items
2. Look at each item card
3. Should see small circular owner avatar with name

---

### My Lended Items - Borrower Avatars
**Where:** http://127.0.0.1:8000/my-lended-items/

**Check:**
- [ ] Borrower profile picture on pending requests
- [ ] Size: 48x48 pixels (w-12 h-12)
- [ ] Gradient fallback with borrower's initial
- [ ] Next to borrower's name and contact info

**Test:**
1. If you have pending rental requests
2. Go to My Lended Items
3. Check pending requests section
4. Should see borrower's profile picture

---

## 🎨 Visual Elements to Verify

### Gradient Backgrounds
**Profile Stats Cards:**
- 📦 Items Listed: Purple gradient (purple-400 to purple-600)
- 🛒 Items Borrowed: Blue gradient (blue-400 to blue-600)
- 🤝 Items Lent: Green gradient (green-400 to green-600)
- ⚡ Active Rentals: Pink gradient (pink-400 to pink-600)

**Avatar Fallbacks:**
- Purple → Pink → Red gradient
- White text with first letter uppercase
- Consistent across all avatar sizes

### Status Color Coding
- **Green:** Active, approved, success
- **Blue:** Information, approved requests
- **Yellow:** Pending, attention needed
- **Red:** Rejected, declined
- **Gray:** Completed, archived

### Responsive Design
**Test on different screen sizes:**
- [ ] Mobile (< 640px): Cards stack vertically
- [ ] Tablet (640-1024px): 2 columns
- [ ] Desktop (> 1024px): 3-4 columns
- [ ] Profile images maintain aspect ratio

---

## 🔄 User Flow Testing

### Complete Rental Flow (Borrower):
1. [ ] Browse items on home page
2. [ ] See owner avatars on item cards
3. [ ] Click item to view details
4. [ ] See owner profile picture and contact info
5. [ ] Click "Request to Rent"
6. [ ] Fill rental dates and notes
7. [ ] Submit request
8. [ ] Go to "My Rented Items"
9. [ ] See request in "Pending" section (yellow)
10. [ ] Wait for approval
11. [ ] Once approved, appears in "Approved" section (blue)
12. [ ] After pickup, moves to "Active" section (green)
13. [ ] After return, moves to "Completed" section (gray)

### Complete Rental Flow (Lender):
1. [ ] List an item
2. [ ] Wait for rental requests
3. [ ] Notification badge appears on navbar
4. [ ] Go to "My Lended Items"
5. [ ] See request in "Pending Requests"
6. [ ] View borrower profile picture and contact
7. [ ] Click "Accept Request" (green button)
8. [ ] Success message appears
9. [ ] Request moves to "Active Lendings"
10. [ ] After return, moves to "Completed Lendings"

### Profile Management Flow:
1. [ ] Click profile icon in navbar
2. [ ] View profile page with stats
3. [ ] See all your listed items
4. [ ] Click "Change Password"
5. [ ] Submit new password
6. [ ] Success message appears
7. [ ] Return to profile
8. [ ] User still logged in

---

## 📊 Data Verification

### Statistics Accuracy
On profile page, verify these numbers are correct:

**Items Listed:** Should equal the number of Item objects where owner=current_user
```python
Item.objects.filter(owner=request.user).count()
```

**Items Borrowed:** Should equal active/approved rentals where borrower=current_user
```python
Rental.objects.filter(
    borrower=request.user,
    status__in=['pending', 'approved', 'borrowed']
).count()
```

**Items Lent:** Should equal active lendings where lender=current_user
```python
Rental.objects.filter(
    lender=request.user,
    status__in=['approved', 'borrowed']
).count()
```

**Active Rentals:** Should equal currently active transactions
```python
Rental.objects.filter(
    Q(borrower=request.user) | Q(lender=request.user),
    status='borrowed'
).count()
```

---

## 🐛 Common Issues to Check

### Image Upload Issues
- [ ] **Issue:** User image not appearing
  - **Check:** File uploaded during registration?
  - **Check:** MEDIA_URL and MEDIA_ROOT configured?
  - **Check:** Media serving enabled in urls.py?
  - **Solution:** Upload new image or check settings.py

- [ ] **Issue:** Image appears stretched or distorted
  - **Check:** CSS includes `object-cover` class?
  - **Check:** Circular container has fixed aspect ratio?
  - **Solution:** Add object-cover to img tags

### Profile Page Issues
- [ ] **Issue:** Statistics showing 0 when should have data
  - **Check:** Rental objects have correct foreign keys?
  - **Check:** Status field uses correct names?
  - **Solution:** Verify database relationships

- [ ] **Issue:** Items not showing in grid
  - **Check:** Items have owner=current_user?
  - **Check:** Template loop syntax correct?
  - **Solution:** Check Item.objects.filter(owner=request.user)

### Password Change Issues
- [ ] **Issue:** User logged out after password change
  - **Check:** `update_session_auth_hash()` called?
  - **Solution:** Add to password_change_view

- [ ] **Issue:** Form validation errors
  - **Check:** Old password correct?
  - **Check:** New password meets requirements?
  - **Check:** Confirmation matches new password?

### Rental Status Issues
- [ ] **Issue:** Items appearing in wrong section
  - **Check:** Status field value matches filter?
  - **Check:** Status choices in model correct?
  - **Solution:** Verify status names: 'pending', 'approved', 'borrowed', 'returned', 'rejected'

---

## ✅ Success Criteria

### All features working if:
✅ Profile page loads with correct stats  
✅ User images display throughout site  
✅ Password change works without logout  
✅ My Rented Items shows categorized rentals  
✅ My Lended Items has working accept/reject buttons  
✅ Gradient fallbacks appear when no images  
✅ All buttons and links navigate correctly  
✅ Color coding is consistent and meaningful  
✅ Responsive design works on all screen sizes  
✅ No console errors or broken images  

---

## 🎉 Testing Complete

If all checkboxes are marked, the profile features are **fully functional**!

**Next Steps:**
1. Test with multiple users
2. Test edge cases (no items, no rentals)
3. Test on mobile devices
4. Add more users and create realistic data
5. Consider implementing suggested enhancements from PROFILE_FEATURES_GUIDE.md

**Report Issues:**
- Screenshot any bugs
- Note the URL where issue occurred
- Describe expected vs actual behavior
- Check browser console for errors

---

**Server Running:** http://127.0.0.1:8000/  
**Ready for testing!** 🚀
