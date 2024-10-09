from django import template

register = template.Library()

@register.filter
def total_price(cart_items):
    total = 0
    for item in cart_items:
        total += item.product.price * item.quantity
    return total
