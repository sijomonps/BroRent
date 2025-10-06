# pages/views.py

from django.shortcuts import render
from .models import Item # 1. Import the Item model
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm

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

@login_required(login_url='login')
def home_page_view(request):
    all_items_list = Item.objects.all()
    context = {
        'all_items': all_items_list,
    }
    return render(request, 'index.html', context)

@login_required(login_url='login')
def item_detail_view(request, pk):
    item = Item.objects.get(pk=pk) # Get one item by its primary key (pk)
    context = {
        'item': item,
    }
    return render(request, 'item_detail.html', context)

# pages/views.py
from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

@login_required(login_url='login')
def item_list_view(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

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
    if request.method == 'POST':
        item.delete()
        return redirect('home')
    
    context = {'item': item}
    return render(request, 'item_confirm_delete.html', context)