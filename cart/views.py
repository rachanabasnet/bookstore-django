from django.shortcuts import render

from cart.models import CartItem


# Create your views here.
def cart(request):
    user_cart = request.user.cart.filter(is_active=True).first()
    if user_cart:
        items = CartItem.objects.filter(cart=user_cart)
        cart_data = {
        'subtotal': user_cart.get_total(),
        'shipping': 5.99,
        'total': user_cart.get_total() + 5.99,
        }
    else :
        items = CartItem.objects.none()
        cart_data = {}

    return render(request, 'cart.html', {'cart': cart_data, 'items': items})