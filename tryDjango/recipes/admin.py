from django.contrib import admin
# Register your models here.
from django.contrib.auth import get_user_model
from .models import Recipe, RecipeIngredient
User =get_user_model()
admin.site.unregister(User)
class RecipeInline(admin.StackedInline):
    model = Recipe
    extra =0

class UserAdmin(admin.ModelAdmin):
    model = User
    inlines = [RecipeInline]

admin.site.register(User, UserAdmin)
class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra =0
    readonly_fields = ['quantity_as_float']
    # fields =["name", "quantity", "unit", "directions"]

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ["name", "user"]
    readonly_fields = ["timestamp", "updated"]
    raw_id_fields =["user"]
admin.site.register(Recipe, RecipeAdmin)



# Overridding User Model IN This way is Not recommended -->
# from django.contrib.auth import get_user_model
# User = get_user_model()
# admin.site.unregister(User)

# class RecipeInline(admin.StackedInline):
#     model = Recipe
#     extra =0
# class UserAdmin(admin.ModelAdmin):
#     inlines =[RecipeInline]
#     list_display = ["username"]

# admin.site.register(User, UserAdmin)