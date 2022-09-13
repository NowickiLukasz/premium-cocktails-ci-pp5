from django.shortcuts import render


def all_recipes(request):
    """
    Allows to view recipes all recipes
    """

    template = 'recipes/recipes.html'
    return render(request, template)