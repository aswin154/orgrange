from django.contrib import admin
from .models import Cart, CartItems


class ItemsInline(admin.TabularInline):
    model = CartItems
    extra = 0
    fields = ("product", "quantity", "special_price",)


class CartAdmin(admin.ModelAdmin):
    inlines = [ItemsInline]


# Register your models here.
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItems)
