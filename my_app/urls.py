from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('foods/', views.food_index, name='food-index'),
  path('foods/<int:food_id>/', views.food_detail, name='food-detail'),
  path('foods/create/', views.FoodCreate.as_view(), name='food-create'),
  path('foods/<int:pk>/update/', views.FoodUpdate.as_view(), name='food-update'),
  path('foods/<int:pk>/delete/', views.FoodDelete.as_view(), name='food-delete'),
  path('foods/<int:food_id>/add-feeding', views.add_feeding, name='add-feeding'),
  path('ingredients/create/', views.IngredientCreate.as_view(), name='ingredient-create'),
  path('ingredients/<int:pk>/', views.IngredientDetail.as_view(), name='ingredient-detail'),
  path('ingredients/', views.IngredientList.as_view(), name='ingredient-index'),
  path('ingredients/<int:pk>/update/', views.IngredientUpdate.as_view(), name='ingredient-update'),
  path('ingredients/<int:pk>/delete/', views.IngredientDelete.as_view(), name='ingredient-delete'),
  path('foods/<int:food_id>/associate-ingredient/<int:ingredient_id>', views.associate_ingredient, name='associate-ingredient'),
  path('foods/<int:food_id>/remove-ingredient/<int:ingredient_id>/', views.remove_ingredient, name='remove-ingredient'),
  path('admin/', admin.site.urls),
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/signup/', views.signup, name='signup'),

]