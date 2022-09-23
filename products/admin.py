from django.contrib import admin
from .models import Product, Category, ProductReview


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'abv',
        'category',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'title',
    )
    readonly_fields = (
        'user',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductReview, ReviewAdmin)
