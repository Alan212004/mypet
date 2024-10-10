#templatetags/cart_filters.py
from django import template

register = template.Library()

@register.filter
def total_price(cart_items):
    """Calculates total price of all items in the cart."""
    total = sum(item.product.price * item.quantity for item in cart_items)
    return total
