# pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('item/<int:pk>/', views.item_detail_view, name='item_detail'), # Add this line
    path('item/new/', views.create_item_view, name='item_create'), # Add this line
    path('item/<int:pk>/edit/', views.update_item_view, name='item_update'), # Add this
    path('item/<int:pk>/delete/', views.delete_item_view, name='item_delete'), # Add this
    path('items/', views.item_list_view, name='item_list'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]