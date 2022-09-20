from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .models import ContactUs

from .forms import ContactUsForm


def contact_us(request):
    """Allows users to contact site owner"""

    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST, request.FILES)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Message has been sent! Thank you.')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to send message. Please ensure the form is valid.')
    else:
        contact_form = ContactUsForm()

    template = 'contact/contact_us.html'
    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)


def contact_us_list(request):
    submitions = ContactUs.objects.all()

    template = 'contact/contact_us_list.html'

    context = {
        'submitions': submitions,
    }

    return render(request, template, context)


def contact_us_details(request, contact_id):
    """Allows the site owner to view users submisions"""

