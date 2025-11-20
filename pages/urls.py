# pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Admin Reports
    path('admin-reports/', views.admin_reports_dashboard, name='admin_reports'),
    path('reports/items/pdf/', views.export_items_report_pdf, name='export_items_pdf'),
    path('reports/items/excel/', views.export_items_report_excel, name='export_items_excel'),
    path('reports/rentals/pdf/', views.export_rentals_report_pdf, name='export_rentals_pdf'),
    path('reports/rentals/excel/', views.export_rentals_report_excel, name='export_rentals_excel'),
    path('reports/users/pdf/', views.export_users_report_pdf, name='export_users_pdf'),
    path('reports/users/excel/', views.export_users_report_excel, name='export_users_excel'),
    
    path('item/<int:pk>/rent/', views.rental_request_view, name='rental_request'),
    path('notifications/', views.notifications_list_view, name='notifications'),
    path('notifications/<int:pk>/read/', views.notification_mark_read_view, name='notification_mark_read'),
    path('rental/<int:pk>/accept/', views.rental_request_accept_view, name='rental_accept'),
    path('rental/<int:pk>/reject/', views.rental_request_reject_view, name='rental_reject'),
    path('', views.landing_view, name='landing'),
    path('home/', views.home_page_view, name='home'),
    path('item/<int:pk>/', views.item_detail_view, name='item_detail'),
    path('item/new/', views.create_item_view, name='item_create'),
    path('item/<int:pk>/edit/', views.update_item_view, name='item_update'),
    path('item/<int:pk>/delete/', views.delete_item_view, name='item_delete'),
    path('items/', views.item_list_view, name='item_list'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
    path('password-change/', views.password_change_view, name='password_change'),
    path('my-rented-items/', views.my_rented_items_view, name='user_items'),
    path('my-lended-items/', views.my_lended_items_view, name='user_lended_items'),
]