from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import FoodItem
from .forms import FoodItemForm

def home(request):
    return render(request, 'home.html')

def food_list(request):
    foods = FoodItem.objects.all()
    return render(request, 'food_list.html', {'foods': foods})

def food_detail(request, pk):
    food = get_object_or_404(FoodItem, pk=pk)
    return render(request, 'food_detail.html', {'food': food})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def all_foods(request):
    foods = FoodItem.objects.all()
    return render(request, 'foods/all_foods.html', {'foods': foods})

@login_required
def add_food(request):
    if request.method == "POST":
        form = FoodItemForm(request.POST)
        if form.is_valid():
            food = form.save(commit=False)
            food.user = request.user  # Asigna el usuario actual
            food.save()
            return redirect('all_foods')  # Redirige a la lista de alimentos
    else:
        form = FoodItemForm()

    return render(request, 'foods/add_food.html', {'form': form})

@login_required
def food_update(request, pk):
    food = get_object_or_404(FoodItem, pk=pk)
    if request.method == "POST":
        form = FoodItemForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodItemForm(instance=food)
    return render(request, 'food_form.html', {'form': form})

@login_required
def food_delete(request, pk):
    food = get_object_or_404(FoodItem, pk=pk)
    if request.method == "POST":
        food.delete()
        return redirect('food_list')
    return render(request, 'food_confirm_delete.html', {'food': food})