from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product


def all_products(request):
    """
    A view to show image links to products, books or recipes
    """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter any search words!")
                return redirect(reverse('home'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query
    }
    return render(request, 'products/products.html', context)


def all_cocktails(request):
    """
    A view to show image links to products, books or recipes
    """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/cocktails.html', context)


def all_books(request):
    """
    A view to show image links to products, books or recipes
    """

    books = Product.objects.all()
    # books = product.filter(category)

    context = {
        'books': books,
    }
    return render(request, 'products/books.html', context)


def book_details_page(request, product_id):
    """
    Displays details of a single book item.
    """

    book = get_object_or_404(Product, pk=product_id)
    
    context = {
        'book': book,

    }

    return render(request, 'products/book_details_page.html', context)