from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_recipes, name='all_recipes'),
    path('recipe_details/<int:recipe_id>/', views.recipe_details, name='recipe_details'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('add_recipe_ingredient/<int:recipe_id>', views.add_recipe_ingredient, name='add_recipe_ingredient'),
    path('edit_recipe/<int:recipe_id>', views.edit_recipe, name='edit_recipe'),
    path('edit_recipe_ingredients/<int:recipe_id>', views.edit_recipe_ingredients, name='edit_recipe_ingredients'),
    path('delete_recipe/<int:recipe_id>', views.delete_recipe, name='delete_recipe'),
]
