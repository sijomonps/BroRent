# pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
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
    path('profile/', views.home_page_view, name='profile'),  # Temporary redirect to home
    path('password-change/', views.home_page_view, name='password_change'),  # Temporary redirect to home
    path('my-items/', views.home_page_view, name='user_items'),  # Temporary redirect to home
    path('my-lended-items/', views.home_page_view, name='user_lended_items'),  # Temporary redirect to home
]