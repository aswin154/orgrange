from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    quantity = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    price = models.IntegerField()

    image = models.ImageField(upload_to='products', blank=True, null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
