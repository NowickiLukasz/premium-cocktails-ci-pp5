from django import forms
from django.forms.models import inlineformset_factory
from .models import Recipe, RecipeIngredient


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        exclude = ('user',)


class RecipeIngredientForm(forms.ModelForm):

    class Meta:
        model = RecipeIngredient
        exclude = ('recipe',)


IngredientFormSet = inlineformset_factory(
    Recipe,
    RecipeIngredient,
    form=RecipeIngredientForm,
    can_delete=False,
    min_num=1,
    extra=0,
    )
