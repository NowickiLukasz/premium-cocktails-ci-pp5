from django.shortcuts import render


def profile(request):
    """Display The user account"""

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)