from django.contrib import admin
from .models import FoodItem, Ingredient

# Register your models here.
admin.site.register(FoodItem)
#admin.site.register(Review)
admin.site.register(Ingredient)
