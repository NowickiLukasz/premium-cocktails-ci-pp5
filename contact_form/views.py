from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactUsForm


def contact_us(request):
    """Allows users to contact site owner"""

    contact_form = ContactUsForm()

    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST, request.FILES)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Successfully added item!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to add item. Please ensure the form is valid.')
    else:
        contact_form = ContactUsForm()

    template = 'contact/contact_us.html'
    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)
    # return render(request, template)
