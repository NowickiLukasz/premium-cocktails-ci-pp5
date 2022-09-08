from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm



def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "You have no items in your basket")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LVEsyJwADn4Fd8ynJ50hrYtvRK27ShJYH02nDugpmiSWuu3DceGdyLDdazw9IqMqL0khgafpfGKp0SttTK1URI800Afm8Vwid',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)