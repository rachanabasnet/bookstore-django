from django.urls import path

from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_to_cart/<int:item_id>', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>', views.remove_from_cart, name='remove_from_cart'),
    path('add_quantity_to_cart/<int:item_id>', views.add_quantity_to_cart, name='add_quantity_to_cart'),
    path('reduce_quantity_to_cart/<int:item_id>', views.reduce_quantity_to_cart, name='reduce_quantity_to_cart'),
    path('confirm_order/<int:cart_id>', views.confirm_order, name='confirm_order'),
]