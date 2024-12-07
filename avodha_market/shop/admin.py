from django.contrib import admin
from .models import Category, Product, ProductImage


# Register your models here.

class ImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0
    fields = ("image",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "enabled"]
    list_editable = ["enabled", ]

    prepopulated_fields = {"slug": ("name",)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "quantity", "price", "available", "image", "enabled", ]
    list_editable = ["quantity", "price", "available", "image", "enabled", ]

    prepopulated_fields = {"slug": ("name",)}

    inlines = [ImageInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
