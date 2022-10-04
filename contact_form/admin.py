from django.contrib import admin

from .models import ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    """Admin Class for ContactUs Model"""
    list_display = (
        'name', 'content', 'email', 'created_on',
    )
