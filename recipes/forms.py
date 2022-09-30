from django import forms
from django.forms.models import inlineformset_factory
from .models import Recipe, RecipeIngredient


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        exclude = ('user',)


class RecipeIngredientForm(forms.ModelForm):

    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter ingredient here'
        })
    )
    quantity = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter quantity here'
        })
    )
    unit = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter measurement unit here'
        })
    )

    class Meta:
        model = RecipeIngredient
        exclude = ('recipe',)


IngredientFormSet = forms.modelformset_factory(
    RecipeIngredient,
    form=RecipeIngredientForm,
    can_delete=False,
    fields=('name', 'quantity', 'unit',),
    min_num=3,
    max_num=3,
    # extra=2,
    )
