from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product


def view_basket(request):
    """
    A view to render contents of the basket
    """
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """
    Add a selected amount of items to the basket
    """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(
            request, f'Updated {product.name} quantity to "{basket[item_id]}"'
            )

    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {product.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """
    Adjust amount of items in the basket
    """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} quantity to "{basket[item_id]}"'
            )

    else:
        basket.pop(item_id)
        messages.success(request, f'Removed {product.name} from the basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_item_from_basket(request, item_id):
    """
    Removes the selected item from the basket
    """
    product = Product.objects.get(pk=item_id)
    basket = request.session.get('basket', {})

    basket.pop(item_id)
    messages.success(request, f'Removed {product.name} from the basket')

    request.session['basket'] = basket
    return HttpResponse(status=200)
