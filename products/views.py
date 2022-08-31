from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product


def all_products(request):
    """
    A view showing search results from query in search bar
    """

    products = Product.objects.all()
    query = None
    sort = None
    direction = None
    category = None


    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
        
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'q' in request.GET:

            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter any search words!")
                return redirect(reverse('home'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
        
        if 'category' in request.GET:
            categories = request.GET['category']
            products = products.filter(category__title=categories)
    
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_sorting': current_sorting,
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