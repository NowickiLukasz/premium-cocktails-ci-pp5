from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    """A class for contact form"""
    class Meta:
        model = ContactUs
        fields = '__all__'