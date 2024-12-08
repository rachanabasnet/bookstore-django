from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from books.models import Book


# Create your views here.
def index(request):
    template_name = 'index.html'
    return render(request, template_name)


def books(request):
    template_name = 'books.html'
    book_list = Book.objects.all()
    return render(request, template_name, {'books': book_list})