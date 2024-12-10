from django.contrib.auth.models import User
from django.db import models

from cart.models import Cart


# Create your models here.
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