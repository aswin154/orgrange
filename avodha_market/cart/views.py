from django.shortcuts import render, redirect

from shop.models import Product
from .models import Cart, CartItems


# Create your views here.
def create_cart(request):
    pass


def get_cart_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()

    return ct_id


def cart_details(request):
    cart_id = get_cart_id(request)

    try:
        user_cart = Cart.objects.get(cart_id=cart_id)

    except Cart.DoesNotExist:
        return render(request, 'cart.html', {'no_cart': True})

    cart_items = user_cart.cart_items.all()

    total_price = 0
    total_items = 0
    for item in cart_items:
        item_price = item.product.price * item.quantity
        total_price += item_price
        total_items += item.quantity

        item.total_price = item_price

    context = {
        "cart": user_cart,
        "cart_items": cart_items,
        "total_price": total_price,
        "total_items": total_items,
    }

    return render(request, 'cart.html', context)


def add_to_cart(request):
    product_id = request.GET.get('q')

    product = Product.objects.get(pk=product_id)
    cart_id = get_cart_id(request)
    try:
        user_cart = Cart.objects.get(cart_id=cart_id)

    except Cart.DoesNotExist:
        user_cart = Cart.objects.create(cart_id=cart_id)

    try:
        cart_item = CartItems.objects.get(cart=user_cart, product=product)

    except CartItems.DoesNotExist:
        cart_item = CartItems.objects.create(cart=user_cart, product=product)

    return redirect('cart')


def remove_from_cart(request):
    pass
