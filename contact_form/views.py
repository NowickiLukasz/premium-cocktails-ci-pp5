from django.shortcuts import render
# from .forms import ContactUsForm


def contact_us(request):
    """Allows users to contact site owner"""

    # contact_form = ContactUsForm()

    template = 'contact/contact_us.html'
    # context = {
    #     'contact_form': contact_form,
    # }

    # return render(request, template, context)
    return render(request, template)
