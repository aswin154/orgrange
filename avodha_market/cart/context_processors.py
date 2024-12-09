from .models import Cart
from .views import get_cart_id


def cart_values(request):
    if 'admin' in request.path or 'cart' in request.path:
        return {}

    ct_id = get_cart_id(request)

    try:
        cart = Cart.objects.get(cart_id=ct_id)
        item_count = cart.cart_items.count()

    except Cart.DoesNotExist:
        item_count = 0

    return {'cart_item_count': item_count}
