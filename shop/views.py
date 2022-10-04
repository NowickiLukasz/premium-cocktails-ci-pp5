from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import NewsletterForm


def shop_page(request):
    """
    Displays the shop main page.
    Displays sections for books, cocktails and recipes
    """

    return render(request, 'shop/shop.html')


@login_required
def newsletter_application(request):
    """Send a newsletter requast to site owner"""

    if request.method == 'POST':
        newsletter = NewsletterForm(request.POST)
        if newsletter.is_valid():
            newsletter.save()
            messages.success(request, 'You have signed up to our newsletter.')
            return redirect(reverse('home'))

    else:
        newsletter = NewsletterForm()

    template = 'shop/newsletter.html'
    context = {
        'newsletter': newsletter,
    }

    return render(request, template, context)
