from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    """
    user's profile
    """
    user = models.OneToOneField(
        User, related_name="users", on_delete=models.CASCADE)
    # goals = models.ForeignKey(Goals, related_name="goals", on_delete=models.CASCADE, null=True)
    profile_image = CloudinaryField("profile", blank=True, null=True)

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
    user = models.ForeignKey(
        User, related_name="users_recipes", on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self) :
        return self.name

