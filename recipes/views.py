from django.shortcuts import render, get_object_or_404, redirect, reverse


from .models import Recipe, RecipeIngredient
from .forms import RecipeForm, RecipeIngredientForm


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
    recipe_ingredients = RecipeIngredient.objects.all()

    context = {
        'recipe': recipe,
        'recipe_ingredients': recipe_ingredients,
    }

    template = 'recipes/recipe_details.html'
    return render(request, template, context)


def add_recipe(request):
    """Allows superuser to add a recipe to the site"""

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect(reverse('add_recipe_ingredient'))
    else:
        form = RecipeForm()
    
    template = 'recipes/add_recipe.html'

    context = {
        'form': form,
    }
    return render(request, template, context)


def add_recipe_ingredient(request):
    """Allows user to add ingredients to recipe"""

    if request.method == 'POST':
        ingredient_form = RecipeIngredientForm(request.POST, request.FILES)
        if ingredient_form.is_valid():
            new_form = ingredient_form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect(reverse('home'))
    else:
        ingredient_form = RecipeIngredientForm()

    template = 'recipes/add_recipe_ingredient.html'

    context = {
        'ingredient_form': ingredient_form,
    }
    return render(request, template, context)
