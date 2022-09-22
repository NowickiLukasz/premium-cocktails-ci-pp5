from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from .models import Recipe, RecipeIngredient
from .forms import RecipeForm, RecipeIngredientForm, IngredientFormSet


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


def add_recipe(request):
    """Allows superuser to add a recipe to the site"""
    
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            formset = IngredientFormSet(request.POST, instance=recipe)
            
            if formset.is_valid():
                formset.save()
                messages.success(request, 'Successfully added recipe name and method!')
                return redirect(reverse('home'))
    else:
        form = RecipeForm()
        formset = IngredientFormSet()
    
    template = 'recipes/add_recipe.html'

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, template, context)


# def add_recipe(request):
#     """Allows superuser to add a recipe to the site"""
#     if request.method == 'POST':
#         form = RecipeForm(request.POST, request.FILES)
#         if form.is_valid():
#             recipe = form.save(commit=False)
#             recipe.user = request.user
#             recipe.save()
           
#             messages.success(request, 'Successfully added recipe name and method!')
#             return redirect(reverse(''))
#     else:
#         form = RecipeForm()

#     template = 'recipes/add_recipe.html'

#     context = {
#         'form': form,
#     }
#     return render(request, template, context)


# def add_recipe_ingredient(request, pk):
#     """Allows admin to add recipe ingredinets"""
#     recipe = Recipe.objects.get(pk=pk)
#     formset = IngredientFormSet(request.POST)

#     if request.method == 'POST':
#         if formset.is_valid():
#             formset.instance = recipe
#             formset.save()
#             return redirect('recipe_ingredients', pk=recipe.id)

#     context = {
#         'formset': formset,
#     }

#     template = 'recipes/recipe_ingredients.html'
#     return render(request, template, context)


def recipe_details(request, recipe_id):
    """Allows to view a specific recipe"""

    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe_ingredients = RecipeIngredient.objects.filter(recipe=recipe)
    context = {
        'recipe': recipe,
        'recipe_ingredients': recipe_ingredients,
    }

    template = 'recipes/recipe_details.html'
    return render(request, template, context)


def edit_recipe(request, recipe_id):

    """Allows the super user to edit recipe on page"""

    recipe = get_object_or_404(Recipe, id=recipe_id)
    ingredients = RecipeIngredient.objects.filter(recipe=recipe)

    if request.method == 'POST':
        edit_form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if edit_form.is_valid():
            edit_form.save()
            formset = IngredientFormSet(request.POST, instance=ingredients)
            
            if formset.is_valid():
                formset.save()
                messages.success(request, 'Successfully added recipe name and method!')
                return redirect(reverse('home'))
           
        else:
            messages.error(request, 'Failed to update recipe, make sure the form is valid')
    else:
        edit_form = RecipeForm(instance=recipe)
        formset = IngredientFormSet(instance=recipe)

    template = 'recipes/edit_recipe.html'

    context = {
        'edit_form': edit_form,
        'recipe': recipe,
        'formset': formset,
    }
    return render(request, template, context)


def delete_recipe(request, recipe_id):
    """Deletes a recipe from the site"""
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.delete()
    messages.success(request, 'Recipe has been deleted')
    return redirect(reverse('all_recipes'))