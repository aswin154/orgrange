from django.contrib.auth.models import User
from django.db import models

from shop.models import Category, Product


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, related_name='my_cart', on_delete=models.CASCADE, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart-{self.pk}'


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='all_cart_items', on_delete=models.CASCADE)

    quantity = models.IntegerField(default=0)
    special_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Cart Items'

    def __str__(self):
        return f'{self.product.name}'
