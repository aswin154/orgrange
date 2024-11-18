from django.shortcuts import render

from shop.models import Product
from .models import Cart, CartItems


# Create your views here.
def create_cart(request):
    pass


def cart_id(request):
    ct_id = request.session_key
    if not ct_id:
        ct_id = request.session.create()

    return ct_id


def cart_details(request):
    return render(request, 'cart.html')


def add_to_cart(request, product_id):
    pass


def remove_from_cart(request):
    pass
