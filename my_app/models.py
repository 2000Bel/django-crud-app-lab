from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class FoodItem(models.Model):  
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    food = models.ForeignKey(FoodItem, on_delete=models.CASCADE, related_name='ingredients')  
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    foods = models.ManyToManyField(FoodItem, related_name='categories')
    def __str__(self):
        return self.name