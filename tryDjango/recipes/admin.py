from django.contrib import admin

# Register your models here.
from .models import Recipe, RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    list_display = ["name", "user"]
    readonly_fields = ["timestamp", "updated"]
    raw_id_fields =["user"]
admin.site.register(Recipe, RecipeAdmin)


admin.site.register(RecipeIngredient)