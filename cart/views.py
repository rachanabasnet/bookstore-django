from django.contrib import messages
from django.shortcuts import render, redirect

from books.models import Book
from cart.models import CartItem, Cart
from order.models import Order


# Create your views here.
def cart(request):
    user_cart = request.user.cart.filter(is_active=True).first()
    if user_cart:
        items = CartItem.objects.filter(cart=user_cart)
        cart_data = {
            'id': user_cart.id,
            'subtotal': f"{float(user_cart.get_total()):.2f}",
            'shipping': 5.99,
            'total': f"{float(user_cart.get_total() + 5.99):.2f}",
        }
    else :
        items = CartItem.objects.none()
        cart_data = {}

    return render(request,
                  'cart.html',
                  {'cart': cart_data, 'items': items, 'has_items': len(items)})


def add_to_cart(request, item_id):
    user_cart, _ = Cart.objects.get_or_create(user=request.user, is_active=True)

    cart_item = CartItem(book=Book.objects.get(id=item_id), cart=user_cart)
    cart_item.save()

    return redirect('books')


def add_quantity_to_cart(request, item_id):
    try:
        user_cart = Cart.objects.get(user=request.user, is_active=True)
        try:
            cart_item = CartItem.objects.get(id=item_id, cart=user_cart)
            cart_item.quantity += 1
            cart_item.save()
        except CartItem.DoesNotExist:
            messages.error(request, 'Error adding quantity to the cart. Please try again.')
    except Cart.DoesNotExist:
        messages.error(request, 'Error adding quantity to the cart. Please try again.')
    return redirect('cart')

def reduce_quantity_to_cart(request, item_id):
    try:
        user_cart = Cart.objects.get(user=request.user, is_active=True)
        try:
            cart_item = CartItem.objects.get(id=item_id, cart=user_cart)
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()
        except CartItem.DoesNotExist:
            messages.error(request, 'Error adding quantity to the cart. Please try again.')
    except Cart.DoesNotExist:
        messages.error(request, 'Error adding quantity to the cart. Please try again.')
    return redirect('cart')


def remove_from_cart(request, item_id):
    try:
        user_cart = Cart.objects.get(user=request.user, is_active=True)
        try:
            cart_item = CartItem.objects.get(id=item_id, cart=user_cart)
            cart_item.delete()
        except CartItem.DoesNotExist:
            messages.error(request, 'Item not found.')
    except Cart.DoesNotExist:
        messages.error(request, 'Item not found.')
    return redirect('cart')


def confirm_order(request, cart_id):
    try:
        user_cart = Cart.objects.get(id=cart_id)
        user_cart.is_active = False
        user_cart.save()
        order = Order(user=request.user, cart=user_cart)
        order.save()
        messages.success(request, 'Order confirmed.')
    except Cart.DoesNotExist:
        messages.error(request, 'Cart not found. Please try again.')
    return redirect('orders')
