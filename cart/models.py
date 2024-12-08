from django.contrib.auth.models import User
from django.db import models

from books.models import Book


# Create your models here.
# class CartItem(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book_items")
#     quantity = models.PositiveIntegerField(default=1)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_items")
