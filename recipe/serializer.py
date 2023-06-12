from rest_framework import serializers
from .models import Category, Recipes

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class RecipiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = '__all__'

