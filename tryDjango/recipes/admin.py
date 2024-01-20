from django.contrib import admin
# Register your models here.
from .models import Recipe, RecipeIngredient
class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra =0
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