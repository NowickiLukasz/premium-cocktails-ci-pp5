from django.shortcuts import render

def view_basket(request):
    """
    A view to render contents of the basket
    """
    return render(request, 'basket/basket.html')