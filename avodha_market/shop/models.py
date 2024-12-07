import uuid
from datetime import datetime

from django.db import models
from django.template.defaultfilters import slugify

from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True, blank=True)

    enabled = models.BooleanField(default=True, )

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Categories"

    def get_url(self):
        return reverse("products_in_category", args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)

    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, blank=True, null=True)
    manufacturer = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True)
    quantity = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    image = models.ImageField(upload_to="primary_images", blank=True, null=True)

    created_at = models.DateTimeField(blank=True, null=True)
    enabled = models.BooleanField(default=True, )

    class Meta:
        ordering = ("-created_at",)

    def get_url(self):
        return reverse("product_details", args=[self.pk, self.slug])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # save the object to database to get pk
        if not self.pk:
            super(Product, self).save(*args, **kwargs)

        if not self.slug:
            self.slug = f"{slugify(self.name)}"

        if not self.created_at:
            self.created_at = datetime.now()

        super(Product, self).save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name="more_images", on_delete=models.CASCADE)

    image = models.ImageField(upload_to="product_images", blank=True, null=True)

    def __str__(self):
        return f'{self.product.name}-{self.pk}'
