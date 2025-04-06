from django.db import models
from django.urls import reverse
from datetime import date
# Import the User
from django.contrib.auth.models import User


MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)
class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ingredient-detail', kwargs={'pk': self.id})

# Create your models here.
class Food(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  ingredients = models.ManyToManyField(Ingredient)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.name} ({self.id})'
  
  def get_absolute_url(self):
    return reverse('food-detail', kwargs={'food_id': self.id})
  
class Order(models.Model):
  date = models.DateField('Order date')
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )
  food = models.ForeignKey(Food, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']