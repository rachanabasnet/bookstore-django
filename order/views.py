from django.shortcuts import render

from order.models import Order


# Create your views here.
def orders(request):
    template_name = 'orders.html'
    order_list = Order.objects.filter(user=request.user)
    return render(request, template_name, {'orders': order_list, 'order_count': len(order_list)})