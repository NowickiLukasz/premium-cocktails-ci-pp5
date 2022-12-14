from django.db import models

from django.contrib.auth.models import User


MEASURE_UNIT = [
    ('ML', 'ML'),
    ('OZ', 'OZ'),
    ('DASH', 'DASH')
]


class Recipe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes')
    name = models.CharField(max_length=254, blank=False, null=False)
    method = models.TextField()
    image = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients')
    name = models.CharField(max_length=50, blank=False, null=False)
    quantity = models.PositiveSmallIntegerField()
    unit = models.CharField(max_length=50, choices=MEASURE_UNIT, default='ML')

    def __str__(self):
        return self.name
