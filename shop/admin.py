from django.contrib import admin
from .models import Newsletter


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    """Newsletter Class for Newsletter Model"""
    list_display = (
        'email', 'created_on',
    )
