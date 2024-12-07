from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from books.models import Book


# Create your views here.
def index(request):
    template_name = 'index.html'
    return render(request, template_name)


@login_required
def books(request):
    template_name = 'books.html'
    books = Book.objects.all()
    return render(request, template_name, {'books': books})