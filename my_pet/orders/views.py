from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from cart.models import CartItem
from .models import Order, OrderItem


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'order_detail.html', {'order': order})

# Restrict checkout to logged-in users
@login_required
def create_order(request):
    if request.method == 'POST':
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        
        order = Order.objects.create(user=request.user, total_price=total_price)

        # Create OrderItems based on CartItems
        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                price=cart_item.product.price
            )

        # Optionally clear the cart
        cart_items.delete()

        return render(request, 'order_confirmation.html', {'order': order})

    return render(request, 'checkout.html')  # Handle GET request

@login_required
def user_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'user_orders.html', {'orders': orders})

import logging

logger = logging.getLogger(__name__)

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)  # Get the user's cart items
    return render(request, 'checkout.html', {'cart_items': cart_items})



