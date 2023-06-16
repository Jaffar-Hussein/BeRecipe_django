from nturl2path import url2pathname
from django.urls import path
from . import views


urlpatterns=[
    
    path('all_recipies/',views.allRecipies.as_view(), name='recipes'),
    path('all_categories/', views.allCategories.as_view(), name='categories'),
    path('recipies_details/', views.recipies_details.as_view(), name='recipes_details'),
    path('filter_recipes/',views.filter_recipes.as_view(), name='filter_recipes'),
    path('register_user/',views.RegisterView.as_view(),name='register'),


]
