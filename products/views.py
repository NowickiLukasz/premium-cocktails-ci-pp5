from django.shortcuts import render
from .models import Product


def all_products(request):
    """
    A view to show image links to products, books or recipes
    """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)