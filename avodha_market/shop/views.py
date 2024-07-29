from django.shortcuts import render
from .models import Product, Category


# Create your views here.
def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    context = {
        'products': products,
        'categories': categories,
    }

    return render(request, 'home.html', context)
