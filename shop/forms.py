from django import forms
from .models import Newsletter


class NewsletterForm(forms.ModelForm):
    """A class for newsletter"""

    class Meta:
        model = Newsletter
        fields = ('email',)
