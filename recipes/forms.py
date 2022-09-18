from django import forms

from .models import Recipe, RecipeIngredient


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        exclude = ('user',)


class RecipeIngredientForm(forms.ModelForm):

    class Meta:
        model = RecipeIngredient
        exclude = ('recipe',)


