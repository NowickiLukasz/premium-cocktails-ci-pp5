from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_recipes, name='all_recipes'),
    path('recipe_details/<int:recipe_id>/', views.recipe_details, name='recipe_details'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('edit_recipe/<int:recipe_id>', views.edit_recipe, name='edit_recipe'),
    path('delete_recipe/<int:recipe_id>', views.delete_recipe, name='delete_recipe'),
]
