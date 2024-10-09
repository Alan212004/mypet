from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from cart.models import CartItem
from .models import Order

# Restrict checkout to logged-in users
@login_required
def create_order(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    order = Order.objects.create(user=request.user, total_price=total_price)
    order.items.set(cart_items)
    cart_items.delete()
    return render(request, 'order_confirmation.html', {'order': order})

@login_required
def user_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'user_orders.html', {'orders': orders})

