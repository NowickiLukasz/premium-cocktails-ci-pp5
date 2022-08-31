from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from django.contrib import messages
from products.models import Product


def shop_page(request):
    """
    Displays the shop main page.
    Displays sections for books, cocktails and recipes
    """
    
    return render(request, 'shop/shop.html')


# def category(request):

#     products = Product.objects.all()
#     category = None

#     if request.GET:
#         if 'category' in request.GET:
#             categories = request.GET['category']
#             products = products.filter(category__title=categories)

#     context = {
#         'products': products,
#     }
#     return render(request, 'products/products.html', context)
