# pages/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils.timezone import datetime
from django.core.exceptions import PermissionDenied

from .models import Item
from .forms import (
    CustomUserCreationForm,
    CustomAuthenticationForm,
    ItemForm,
    ItemSearchForm
)

def landing_view(request):
    """Landing page for unauthenticated users"""
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'landing.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

from django.contrib.auth.decorators import login_required

from django.db.models import Q
from .forms import ItemSearchForm
from django.utils.timezone import datetime

@login_required(login_url='login')
def home_page_view(request):
    form = ItemSearchForm(request.GET)
    items = Item.objects.all().order_by('-date_posted')

    if form.is_valid():
        # Search by keyword
        if search_query := form.cleaned_data.get('search'):
            items = items.filter(
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query)
            )

        # Filter by category
        if category := form.cleaned_data.get('category'):
            items = items.filter(category=category)

        # Filter by availability
        if form.cleaned_data.get('availability'):
            items = items.filter(is_available=True)

        # Sort items
        if sort_by := form.cleaned_data.get('sort_by'):
            if sort_by == 'price_asc':
                items = items.order_by('price')
            elif sort_by == 'price_desc':
                items = items.order_by('-price')
            elif sort_by == 'date_desc':
                items = items.order_by('-date_posted')
            elif sort_by == 'date_asc':
                items = items.order_by('date_posted')
    else:
        # Default sorting by newest first
        items = items.order_by('-date_posted')

    context = {
        'all_items': items,
        'form': form
    }
    return render(request, 'index.html', context)

@login_required(login_url='login')
def item_detail_view(request, pk):
    item = Item.objects.get(pk=pk) # Get one item by its primary key (pk)
    context = {
        'item': item,
    }
    return render(request, 'item_detail.html', context)



@login_required(login_url='login')
def item_list_view(request):
    form = ItemSearchForm(request.GET)
    items = Item.objects.all()

    if form.is_valid():
        # Search by keyword
        if search_query := form.cleaned_data.get('search'):
            items = items.filter(
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query)
            )

        # Filter by category
        if category := form.cleaned_data.get('category'):
            items = items.filter(category=category)

        # Filter by availability
        if form.cleaned_data.get('availability'):
            items = items.filter(is_available=True)

        # Filter by date range
        if date_from := form.cleaned_data.get('date_from'):
            items = items.filter(date_posted__gte=datetime.combine(date_from, datetime.min.time()))
        if date_to := form.cleaned_data.get('date_to'):
            items = items.filter(date_posted__lte=datetime.combine(date_to, datetime.max.time()))

        # Sort items
        if sort_by := form.cleaned_data.get('sort_by'):
            if sort_by == 'price_asc':
                items = items.order_by('price')
            elif sort_by == 'price_desc':
                items = items.order_by('-price')
            elif sort_by == 'date_desc':
                items = items.order_by('-date_posted')
            elif sort_by == 'date_asc':
                items = items.order_by('date_posted')

    context = {
        'items': items,
        'form': form
    }
    return render(request, 'item_list.html', context)

@login_required(login_url='login')
def create_item_view(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm()

    context = {'form': form}
    return render(request, 'item_form.html', context)

@login_required(login_url='login')
def update_item_view(request, pk):
    item = get_object_or_404(Item, pk=pk)
    # Only the owner or a superuser can update
    if not (request.user == item.owner or request.user.is_superuser):
        raise PermissionDenied()
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm(instance=item)
    
    context = {'form': form}
    return render(request, 'item_form.html', context)

@login_required(login_url='login')
def delete_item_view(request, pk):
    item = get_object_or_404(Item, pk=pk)
    # Only the owner or a superuser can delete
    if not (request.user == item.owner or request.user.is_superuser):
        raise PermissionDenied()
    if request.method == 'POST':
        item.delete()
        return redirect('home')
    
    context = {'item': item}
    return render(request, 'item_confirm_delete.html', context)