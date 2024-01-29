from django.db import models
from django.conf import settings
# Create your models here.
from .validators import validate_unit_of_measure
"""
- Global
    - Ingredients
    - Recipes
- User
    - Ingredients
    - Recipes
        - Ingredients
        - Directions for Ingredients

"""
class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    name =models.CharField(max_length =220)
    description =models.TextField(blank =True, null = True)
    directions =models.TextField(blank =True, null = True)
    timestamp =models.DateTimeField(auto_now_add = True)
    updated =models.DateTimeField(auto_now = True)
    active =models.BooleanField(default =True)

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete= models.CASCADE)
    name =models.CharField(max_length =220)
    quantity =models.CharField(max_length =50 ) # 1, 1/4
    #pounds, lbs, oz, gram ,etc
    unit = models.CharField(max_length =50, validators = [validate_unit_of_measure]) 
    description =models.TextField(blank =True, null = True)
    directions =models.TextField(blank =True, null = True)
    timestamp =models.DateTimeField(auto_now_add = True)
    updated =models.DateTimeField(auto_now = True)
    active =models.BooleanField(default =True)
