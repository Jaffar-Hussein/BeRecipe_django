from django.shortcuts import render
from .models import Category, Recipes
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import CategoriesSerializer, RecipiesSerializer
# Create your views here.

#get all categories
class allCategories(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data)

class allRecipies(APIView):
    def get(self, request):
        recipes = Recipes.objects.all()
        serializer = RecipiesSerializer(recipes, many=True)
        return Response(serializer.data)
class recipies_details(APIView):
    def get(self, request):
        if 'rec' in request.GET and request.GET['rec']:
            rec = request.GET['rec']
            recipes = Recipes.objects.filter(category__id=rec)
        else:
            recipes = Recipes.objects.all()
        serializer = RecipiesSerializer(recipes, many=True)
        return Response(serializer.data)

