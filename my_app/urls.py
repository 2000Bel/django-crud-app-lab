from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('foods/', views.food_list, name='food_list'),
    path('foods/<int:pk>/', views.food_detail, name='food_detail'),
    path('foods/create/', views.food_create, name='food_create'),
    path('foods/<int:pk>/update/', views.food_update, name='food_update'),
    path('foods/<int:pk>/delete/', views.food_delete, name='food_delete'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]