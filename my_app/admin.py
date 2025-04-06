from django.contrib import admin
from .models import Food, Feeding, Ingredient

# Register your models here.
admin.site.register(Food)
admin.site.register(Feeding)
admin.site.register(Ingredient)