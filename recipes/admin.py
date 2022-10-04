from django.contrib import admin
from .models import Recipe, RecipeIngredient

# Register your models here.


class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ['user', 'name']
    readonly_fields = ['user', 'date_created']


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient)
