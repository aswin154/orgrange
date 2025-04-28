from django.contrib import admin
from .models import SiteSettings


# Register your models here.
@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'allow_registration', 'allow_user_products')
