# import uuid

from django.db import models
from django.template.defaultfilters import slugify

from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    # def get_url(self):
    #     return reverse()

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)
    description = models.TextField(blank=True)
    quantity = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    price = models.IntegerField()

    image = models.ImageField(upload_to='products', blank=True, null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f'{slugify(self.name)}'
            # self.slug = f'{slugify(self.name)}-{str(uuid.uuid4())[:13]}'

        super(Product, self).save(*args, **kwargs)
