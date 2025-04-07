from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Food, Ingredient
from .forms import OrderForm
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Home(LoginView):
    template_name = 'home.html'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def food_index(request):
  foods = Food.objects.filter(user=request.user)
  return render(request, 'foods/index.html', { 'foods': foods })

@login_required
def food_detail(request, food_id):
    food = Food.objects.get(id=food_id)
    ingredients_food_doesnt_have = Ingredient.objects.exclude(id__in = food.ingredients.all().values_list('id'))

    order_form = OrderForm()
    return render(request, 'foods/detail.html', {
        'food': food,
        'order_form': order_form,
        'ingredients': ingredients_food_doesnt_have
    })

class FoodCreate(LoginRequiredMixin, CreateView):
  model = Food
  fields = ['name', 'description']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class FoodUpdate(LoginRequiredMixin, UpdateView):
  model = Food
  fields = ['description']

class FoodDelete(LoginRequiredMixin, DeleteView):
  model = Food
  success_url = '/food/'

@login_required
def add_order(request, food_id):
  form = OrderForm(request.POST)

  if form.is_valid():
    new_order = form.save(commit=False)
    new_order.food_id = food_id
    new_order.save()
  
  return redirect('food-detail', food_id=food_id)

class IngredientCreate(LoginRequiredMixin, CreateView):
  model = Ingredient
  fields = ['name', 'color']

class IngredientList(LoginRequiredMixin, ListView):
  model = Ingredient

class IngredientDetail(LoginRequiredMixin, DetailView):
  model = Ingredient

class IngredientUpdate(LoginRequiredMixin, UpdateView):
  model = Ingredient
  fields = ['name', 'color']

class IngredientDelete(LoginRequiredMixin, DeleteView):
  model = Ingredient
  success_url = '/ingredients/'

@login_required
def associate_ingredient(request, food_id, ingredient_id):
  Food.objects.get(id=food_id).ingredients.add(ingredient_id)
  return redirect('food-detail', food_id=food_id)

@login_required
def remove_ingredient(request, food_id, ingredient_id):
  food = Food.objects.get(id=food_id)
  ingredient = Ingredient.objects.get(id=ingredient_id)
  food.ingredients.remove(ingredient_id)
  return redirect('food-detail', food_id=food.id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('food-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
