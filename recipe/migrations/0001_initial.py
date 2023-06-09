# Generated by Django 4.2.1 on 2023-06-08 23:54

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "category_image",
                    cloudinary.models.CloudinaryField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="book_category",
                    ),
                ),
                ("description", models.CharField(max_length=100)),
                ("is_fav", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Recipes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=100)),
                ("time", models.CharField(max_length=100)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recipe.category",
                    ),
                ),
            ],
        ),
    ]
