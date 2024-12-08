from django.contrib import admin

from cart.models import Cart, CartItem, Order

# Register your models here.
admin.site.register([
    Cart,
    CartItem,
    Order
])