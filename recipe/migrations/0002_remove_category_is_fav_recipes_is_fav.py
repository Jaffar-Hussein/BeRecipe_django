# Generated by Django 4.2.1 on 2023-06-09 00:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipe", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="is_fav",
        ),
        migrations.AddField(
            model_name="recipes",
            name="is_fav",
            field=models.BooleanField(default=False),
        ),
    ]
