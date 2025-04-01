from django.shortcuts import render
from .models import FoodItem
from .forms import FoodItemForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'my_app/home.html')

@login_required
def food_list(request):
    foods = FoodItem.objects.filter(user=request.user)
    return render(request, 'my_app/food_list.html', {'foods': foods})

@login_required
def food_detail(request, pk):
    food = get_object_or_404(FoodItem, pk=pk, user=request.user)
    return render(request, 'my_app/food_detail.html', {'food': food})

@login_required
def food_create(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            food = form.save(commit=False)
            food.user = request.user
            food.save()
            return redirect('food_list')
    else:
        form = FoodItemForm()
    return render(request, 'my_app/food_form.html', {'form': form})

@login_required
def food_update(request, pk):
    food = get_object_or_404(FoodItem, pk=pk, user=request.user)
    if request.method == 'POST':
        form = FoodItemForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodItemForm(instance=food)
    return render(request, 'my_app/food_form.html', {'form': form})

@login_required
def food_delete(request, pk):
    food = get_object_or_404(FoodItem, pk=pk, user=request.user)
    if request.method == 'POST':
        food.delete()
        return redirect('food_list')
    return render(request, 'my_app/food_confirm_delete.html', {'food': food})

@login_required
def ingredient_create(request, pk):
    food = get_object_or_404(FoodItem, pk=food_pk, user=request.user)
    if request.method == 'POST':
        name = request.POST.get('name')
        Ingredients.objects.create(food=food, name=name)
        return redirect('food_detail', pk=food.pk)
    return render(request, 'my_app/ingredient_form.html', {'food': food})