"""Admin classes for honeypot-signals application."""

from django.contrib import admin

from honeypot-signals.models import Example


class ExampleAdmin(admin.ModelAdmin):
    """Admin class for Example model class."""
    pass


admin.site.register(Example, ExampleAdmin)
