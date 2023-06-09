from django.shortcuts import render
from .models import Category, Recipes
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import CategoriesSerializer, RecipiesSerializer, RegisterSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated,AllowAny

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
            if rec == 'all':
                recipes = Recipes.objects.all()
            else:
                recipes = Recipes.objects.filter(category__id=rec)
            
        else:
            recipes = Recipes.objects.all()
        serializer = RecipiesSerializer(recipes, many=True)
        return Response(serializer.data)

class filter_recipes(APIView):
    def get(self, request):
        if 'id' in request.GET and request.GET['id']:
            rec = request.GET['id']
            specific_Rec = Recipes.objects.filter(id=rec)

        serializer = RecipiesSerializer(specific_Rec, many=True)
        return Response(serializer.data)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

