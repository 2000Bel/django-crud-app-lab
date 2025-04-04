from django.urls import path
from .views import all_foods, add_food
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('foods/all_foods/', all_foods, name='all_foods'),
    path('foods/add_food/', add_food, name='add_food'),
    path('foods/', views.food_list, name='food_list'),
    path('foods/<int:pk>/', views.food_detail, name='food_detail'),
    path('foods/<int:pk>/update/', views.food_update, name='food_update'),
    path('foods/<int:pk>/delete/', views.food_delete, name='food_delete'),
    path('signup/', views.signup, name='signup'),
]