from django.contrib import admin
from .models import Category, Recipes

# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    list_display =("name", "description")
    list_filter =("name","description")
    
class recipesAdmin(admin.ModelAdmin):
    list_display=("name", "description", "time", "category","is_fav")
    list_filter =("time", "is_fav")
    # @admin.display(description='categories', ordering='category__name')
    # def get_recipes_name(self, obj):
    #     return obj.category.name

all = [(Category,categoryAdmin),(Recipes,recipesAdmin)]

for i in all:
    admin.site.register(i[0],i[1])