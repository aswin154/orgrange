from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:category_slug>', views.home, name='products_in_category'),
    path('product/<slug:product_slug>', views.product, name='product_details'),
    path('search/', views.search, name='search'),
]
