from django.db import models

from django.contrib.auth.models import User


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=254, blank=False, null=False)
    method = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False, null=False)
    quantity = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)
    