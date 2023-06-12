from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

class Category(models.Model):
    """
    category
    """
    name = models.CharField(max_length=100)
    category_image = CloudinaryField("book_category", blank=True, null=True)
    description = models.CharField(max_length=100)

    def __str__(self) :
        return self.name

class Recipes(models.Model):
    """
    recipes
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    recipes_image = CloudinaryField("recipes", blank=True, null=True)
    is_fav = models.BooleanField(default=False)


    def __str__(self) :
        return self.name
