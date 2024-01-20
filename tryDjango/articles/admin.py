from django.contrib import admin

# Register your models here.
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display =['id','title' ,'slug','content',"timestamp","updated"]
    search_fields =['title','content']
    raw_id_fields =["user"]
    
admin.site.register(Article ,ArticleAdmin)