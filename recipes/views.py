from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

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
    # recipe_ingredients = RecipeIngredient.objects.all()
    recipe_ingredients = get_object_or_404(RecipeIngredient)

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
            recipe_id = new_form.id
            messages.success(request, 'Successfully added recipe name and method!')
            return redirect(reverse('add_recipe_ingredient', args=[recipe_id]))
    else:
        form = RecipeForm()
    
    template = 'recipes/add_recipe.html'

    context = {
        'form': form,
    }
    return render(request, template, context)




def edit_recipe(request, recipe_id):

    """Allows the super user to edit recipe on page"""

    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == 'POST':
        edit_form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'Recipe updated!')
            return redirect(reverse('edit_recipe_ingredients', args=[recipe.id]))
        else:
            messages.error(request, 'Failed to update recipe, make sure the form is valid')
    else:
        edit_form = RecipeForm(instance=recipe)

    template = 'recipes/edit_recipe.html'

    context = {
        'edit_form': edit_form,
        'recipe': recipe,
    }
    return render(request, template, context)


def delete_recipe(request, recipe_id):
    """Deletes a recipe from the site"""
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.delete()
    messages.success(request, 'Recipe has been deleted')
    return redirect(reverse('all_recipes'))