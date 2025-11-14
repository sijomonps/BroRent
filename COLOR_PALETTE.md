# BroRent - Color Palette Documentation

## 🎨 **Synchronized Color Scheme: Teal & Coral Theme**

This document outlines the beautiful, creative, and synchronized color palette used throughout the BroRent website.

---

## **Primary Colors**

### **Teal (Main Brand Color)**
- **Teal-500**: `#14b8a6` - Primary buttons, main CTAs
- **Teal-600**: `#0d9488` - Hover states, emphasis
- **Teal-50**: `#f0fdfa` - Light backgrounds
- **Teal-100**: `#ccfbf1` - Borders, subtle accents

### **Cyan (Secondary Brand Color)**
- **Cyan-500**: `#06b6d4` - Secondary actions
- **Cyan-600**: `#0891b2` - Hover states
- **Cyan-50**: `#ecfeff` - Light backgrounds
- **Cyan-100**: `#cffafe` - Borders

### **Rose/Coral (Accent Color)**
- **Rose-500**: `#f43f5e` - Important alerts, deletions
- **Pink-500**: `#ec4899` - Secondary accents
- **Rose-100**: `#ffe4e6` - Light alert backgrounds

---

## **Secondary Colors**

### **Emerald (Success States)**
- **Emerald-500**: `#10b981` - Available items
- **Emerald-800**: `#065f46` - Success text
- **Emerald-100**: `#d1fae5` - Success backgrounds

### **Amber (Warning/Edit States)**
- **Amber-500**: `#f59e0b` - Edit buttons
- **Orange-500**: `#f97316` - Warning states

---

## **Color Usage Guide**

### **Navigation & Header**
- Background: `from-teal-50 via-cyan-50 to-rose-50` (gradient)
- Border: `border-teal-100`
- Logo: `from-teal-600 to-cyan-600` (gradient text)
- Nav Links: `text-gray-700` → `hover:text-teal-600`
- Profile Avatar: `from-teal-500 to-cyan-500` (gradient)

### **Buttons**
- **Primary CTA**: `from-teal-500 to-cyan-600` → `hover:from-teal-600 to-cyan-700`
- **Edit**: `from-amber-500 to-orange-500`
- **Delete**: `from-rose-500 to-pink-500`
- **Search**: `from-teal-500 to-cyan-600`

### **Item Cards**
- Border: `border-gray-100` → `hover:border-teal-200`
- Image Background: `from-teal-50 to-cyan-50`
- Category Badge: `from-teal-500 to-cyan-500`
- Available Badge: `bg-emerald-100 text-emerald-800 border-emerald-200`
- Rented Badge: `bg-rose-100 text-rose-800 border-rose-200`
- Price: `from-teal-600 to-cyan-600` (gradient text)

### **Dropdown Menu**
- Header Background: `from-teal-50 to-cyan-50`
- Profile: `hover:bg-teal-50 hover:text-teal-600`
- Edit Profile: `hover:bg-cyan-50 hover:text-cyan-600`
- Password: `hover:bg-sky-50 hover:text-sky-600`
- Rented Items: `hover:bg-emerald-50 hover:text-emerald-600`
- Lended Items: `hover:bg-amber-50 hover:text-amber-600`
- Logout: `text-rose-600 hover:bg-rose-50`

### **Notifications**
- Badge: `bg-rose-500` (red for unread count)
- Icon Hover: `hover:text-teal-600`

---

## **Gradient Combinations**

### **Popular Gradients Used**
1. **Primary Gradient**: `from-teal-500 to-cyan-600`
2. **Background Gradient**: `from-teal-50 via-cyan-50 to-rose-50`
3. **Success Gradient**: `from-emerald-500 to-green-500`
4. **Warning Gradient**: `from-amber-500 to-orange-500`
5. **Error Gradient**: `from-rose-500 to-pink-500`
6. **Text Gradient**: `from-teal-600 to-cyan-600`

---

## **Design Principles**

### **Consistency**
- All primary actions use teal-to-cyan gradients
- All destructive actions use rose-to-pink gradients
- All edit actions use amber-to-orange gradients
- All success states use emerald shades

### **Accessibility**
- High contrast between text and backgrounds
- Clear visual hierarchy with color intensity
- Consistent hover states for better UX

### **Modern Aesthetics**
- Soft gradients for visual depth
- Rounded corners (rounded-lg, rounded-xl, rounded-full)
- Subtle shadows for elevation
- Smooth transitions (300ms duration)

---

## **Color Psychology**

- **Teal/Cyan**: Trust, reliability, calmness - perfect for a rental platform
- **Rose/Coral**: Energy, attention, warmth - used for important actions
- **Emerald**: Success, availability, go-ahead signals
- **Amber/Orange**: Caution, modification, attention needed

---

## **Implementation Notes**

All colors use Tailwind CSS utility classes for easy maintenance and consistency:
- Background: `bg-{color}-{shade}`
- Text: `text-{color}-{shade}`
- Border: `border-{color}-{shade}`
- Gradients: `from-{color}-{shade} to-{color}-{shade}`

---

**Last Updated**: October 30, 2025
**Theme Version**: 2.0 - Teal & Coral
