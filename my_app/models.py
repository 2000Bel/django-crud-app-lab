from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class FoodItem(models.Model):  
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    food = models.ManyToManyField(FoodItem, related_name='ingredients')

    def __str__(self):
        return self.name