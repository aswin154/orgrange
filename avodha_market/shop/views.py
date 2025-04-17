from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, InvalidPage

from .models import Product, Category
from cart.models import Cart, CartItems
from cart.views import get_cart_id


# Create your views here.
def home(request, category_slug=None):
    categories = Category.objects.filter(enabled=True)

    if category_slug is None:
        categ_name = "All Categories"
        product_list = Product.objects.filter(enabled=True)[:8]

    else:
        categ = get_object_or_404(Category, slug=category_slug)
        categ_name = categ.name
        product_list = Product.objects.filter(category=categ, enabled=True)[:8]

    paginator = Paginator(product_list, 4)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    context = {
        'home': True,
        'products': products,
        'categories': categories,
        'categ_name': categ_name,
    }

    return render(request, 'home.html', context)


def product(request, pk, product_slug):
    product = get_object_or_404(Product, pk=pk, slug=product_slug)

    categories = Category.objects.filter(enabled=True)
    categ_name = "All Categories"

    ct_id = get_cart_id(request)

    in_cart = CartItems.objects.filter(cart__cart_id=ct_id, product=product).exists()

    context = {
        'product': product,
        'categories': categories,
        'categ_name': categ_name,
        'in_cart': in_cart,
    }

    return render(request, 'product.html', context)


def search(request):
    categories = Category.objects.filter(enabled=True)
    categ_name = "All Categories"

    if 'q' in request.GET:
        query = request.GET.get('q')

        product_list = Product.objects.filter(enabled=True).filter(
            Q(name__icontains=query) | Q(description__icontains=query))

    else:
        product_list = Product.objects.filter(enabled=True)[:8]

    paginator = Paginator(product_list, 12)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    context = {
        'no_search': True,
        'categories': categories,
        'categ_name': categ_name,
        'products': products,
    }
    return render(request, 'search.html', context)
