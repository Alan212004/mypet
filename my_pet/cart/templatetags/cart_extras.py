# templatetags/cart_extras.py
from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiplies the value by the argument"""
    try:
        return value * arg
    except (ValueError, TypeError):
        return ''

@register.simple_tag
def total_price(cart_items):
    """Calculates the total price of items in the cart."""
    return sum(item.product.price * item.quantity for item in cart_items)
