from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from products.models import Product
from .models import CartItem
from django.shortcuts import get_object_or_404

@login_required
def user_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)  # Ensure user attribute exists in CartItem
    return render(request, 'cart.html', {'cart_items': cart_items})

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    # Ensure that the CartItem has a user field, otherwise, you'll need to modify this part
    CartItem.objects.create(product=product, user=request.user)  # Associate the cart item with the user
    return redirect('user_cart')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()  # Remove the item from the cart
    return redirect('user_cart')