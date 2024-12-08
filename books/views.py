from django.shortcuts import render

from books.models import Book
from cart.models import Cart


# Create your views here.
def index(request):
    template_name = 'index.html'
    return render(request, template_name)


def books(request):
    active_cart = Cart.objects.filter(user=request.user, is_active=True).first()
    book_list = []

    if active_cart:
        cart_items = active_cart.items.all()
        cart_books = {item.book.id: item.quantity for item in cart_items}


        for book in Book.objects.all():
            is_in_cart = cart_books.get(book.id, 0)
            book_list.append({'item': book, 'is_in_cart': True if is_in_cart > 0 else False})
    else:
        for book in Book.objects.all():
            book_list.append({'item': book, 'is_in_cart': False})
    return render(request, 'books.html', {'books': book_list})