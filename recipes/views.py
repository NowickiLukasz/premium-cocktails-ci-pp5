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
    
    # form = RecipeForm()
    # formset = IngredientFormSet(queryset=RecipeIngredient.objects.none())

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        formset = IngredientFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            for form in formset:
                data = form.cleaned_data
                if 'quantity' in data:
                    form.instance.recipe = recipe
                    form.save()
            return redirect(reverse('home'))
        else:
            print(form.errors, formset.errors)
            
            # if formset.is_valid():
            #     formset.save()
            #     messages.success(request, 'Successfully added recipe!')
            #     return redirect(reverse('home'))
    else:
        form = RecipeForm()
        formset = IngredientFormSet(queryset=RecipeIngredient.objects.none())

    
    template = 'recipes/add_recipe.html'

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, template, context)


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
    # ingredients = RecipeIngredient.objects.get(recipe=recipe)

    recipe = get_object_or_404(Recipe, id=recipe_id)
    edit_form = RecipeForm(instance=recipe)
    ingredient_formset = IngredientFormSet(queryset=RecipeIngredient.objects.filter(recipe=recipe))

    if request.method == 'POST':
        edit_form = RecipeForm(request.POST, request.FILES, instance=recipe)
        ingredient_formset = IngredientFormSet(request.POST)
        if edit_form.is_valid() and ingredient_formset.is_valid():
            edit_form.save()
            for form in ingredient_formset:
                data = form.cleaned_data
                if 'quantity' in data:
                    form.instance.recipe = recipe
                    form.save()
            messages.success(request, 'Successfully adjusted your recipe!')
            return redirect(reverse('home'))

            # formset = IngredientFormSet(request.POST, instance=ingredients)


            # if ingredient_formset.is_valid():
                
            # if formset.is_valid():
            #     formset.save()
            #     messages.success(request, 'Successfully adjusted your recipe!')
            #     return redirect(reverse('home'))
           
        else:
            edit_form = RecipeForm(request.POST, request.FILES, instance=recipe)
            ingredient_formset = IngredientFormSet(request.POST)
            messages.error(request, 'Failed to update recipe, make sure the form is valid')
    # else:
        # edit_form = RecipeForm(instance=recipe)
        # # formset = IngredientFormSet(instance=recipe)
        # ingredient_formset = IngredientFormSet()

    template = 'recipes/edit_recipe.html'

    context = {
        'edit_form': edit_form,
        'recipe': recipe,
        # 'formset': formset,
        'ingredient_formset': ingredient_formset,
    }
    return render(request, template, context)


def delete_recipe(request, recipe_id):
    """Deletes a recipe from the site"""
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.delete()
    messages.success(request, 'Recipe has been deleted')
    return redirect(reverse('all_recipes'))