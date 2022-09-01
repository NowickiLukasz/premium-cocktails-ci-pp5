from django.shortcuts import get_object_or_404
from products.models import Product

def basket_content(request):

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'products': product,
        })

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'grand_total': total

    }

    return context