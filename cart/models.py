from django.db import models
from django.contrib.auth.models import User

from books.models import Book


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def get_total(self):
        return sum(item.get_total_price() for item in self.items.all())

    def __str__(self):
        return f"Cart {self.id} for {self.user}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.book.price * self.quantity

    def __str__(self):
        return f"{self.cart.user.username}: {self.book.title}"


class Order(models.Model):
    ORDER_STATUS = (
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('canceled', 'Canceled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, related_name='cart_order')
    ordered_at = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=10, choices=ORDER_STATUS, default='pending')

    def __str__(self):
        return f"Order {self.id} by {self.user}"
