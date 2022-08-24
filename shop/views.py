from django.shortcuts import render


def shop_page(request):
    """
    Displays the shop main page.
    Displays sections for books, cocktails and recipes
    """
    return render(request, 'shop/shop.html')