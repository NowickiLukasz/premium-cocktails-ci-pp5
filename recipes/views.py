from django.shortcuts import render, get_object_or_404

from .models import Recipe


def all_recipes(request):
    """
    Allows to view recipes all recipes
    """
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,

    }

    template = 'recipes/recipes.html'
    return render(request, template, context)


def recipe_details(request, recipe_id):
    """Allows to view a specific recipe"""

    recipe = get_object_or_404(Recipe, id=recipe_id)

    context = {
        'recipe': recipe,
    }

    template = 'recipes/recipe_details.html'
    return render(request, template, context)