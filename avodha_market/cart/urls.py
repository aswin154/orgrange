from django.urls import path
from . import views

urlpatterns = [
    path("", views.cart_details, name="cart_details"),
    path("add/<int:product_id>", views.add_to_cart, name="add_to_cart"),
    path("delete/<int:cart_item_id>", views.remove_from_cart, name="remove_from_cart"),
    path("increase/<int:cart_item_id>", views.increase_cart, name="increase_cart"),
    path("decrease/<int:cart_item_id>", views.decrease_cart, name="decrease_cart"),
]
