def bag_content(request):

    bag_items = []
    total = 0
    product_count = 0

    context = {
        'bag_items': bag_items,
        'total': total,
        'prduct_count': product_count,
        'grand_total': total

    }

    return context