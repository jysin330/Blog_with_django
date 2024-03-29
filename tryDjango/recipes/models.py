from django.db import models
from django.conf import settings
from .utils import number_str_to_float
import pint
from django.urls import reverse
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

    def get_absolute_url(self):
        # return '/pantry/recipes/'
        return reverse('recipes:detail', kwargs= {'id': self.id})
    
    def get_edit_url(self):
        return reverse('recipes:update', kwargs= {'id': self.id})

    def get_ingredients_children(self):
        return self.recipeingredient_set.all()
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete= models.CASCADE)
    name =models.CharField(max_length =220)
    quantity =models.CharField(max_length =50 ) # 1, 1/4
    quantity_as_float = models.FloatField(blank = True, null = True)
    #pounds, lbs, oz, gram ,etc
    unit = models.CharField(max_length =50, validators = [validate_unit_of_measure]) 
    description =models.TextField(blank =True, null = True)
    directions =models.TextField(blank =True, null = True)
    timestamp =models.DateTimeField(auto_now_add = True)
    updated =models.DateTimeField(auto_now = True)
    active =models.BooleanField(default =True)

    def get_absolute_url(self):
        return self.recipe.get_absolute_url()
    
    def convert_to_system(self, system ="mks"):
        """
        mks - meter, kilogram, second
        imperial - miles, pounds, second
        """
        if self.quantity_as_float is None:
            return ""
        ureg = pint.UnitRegistry(system = system)
        measurement = self.quantity_as_float * ureg[self.unit]
        
        return measurement #.to_base_units()

    def as_mks(self):
        measurement = self.convert_to_system(system="mks")
        
        return measurement.to_base_units()
        # return measurement.to('kilogram')
    # def as_ounces(self):
    #     measurement = self.convert_to_system()
    #     return measurement.to('ounces')
    
    def as_imperial(self):
        measurement = self.convert_to_system(system="imperial")
        
        return measurement.to_base_units()
        # return measurement.to('pounds')

    def save(self, *args, **kwargs):
        qty = self.quantity
        qty_as_float , qty_as_float_success = number_str_to_float(qty)
        if qty_as_float_success:
            self.quantity_as_float = qty_as_float
        else:
            self.quantity_as_float =None
        super().save(*args, **kwargs)
