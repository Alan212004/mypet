from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .models import Cart, CartItem

@login_required
def user_cart(request):
    # Fetch cart items directly from the user's cart
    cart, created = Cart.objects.get_or_create(user=request.user)  # Get or create the cart for the user
    cart_items = cart.items.all()  # Access items through related name
    return render(request, 'cart.html', {'cart_items': cart_items})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)  # Get or create the cart for the user

    # Check if the item already exists in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1  # If the item already exists, increase the quantity
    cart_item.save()

    return redirect('user_cart')  # Redirect to the user's cart view

@login_required
def remove_from_cart(request, item_id):
    # Fetch the cart item ensuring it belongs to the user's cart
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()  # Remove the item from the cart
    return redirect('user_cart')  # Redirect back to the user's cart

@login_required
def cart_view(request):
    # This function is now redundant with user_cart function
    # It can be removed unless you have specific logic in mind for it
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()  # Retrieve all items for the user's cart
    return render(request, 'cart.html', {'items': items})

@login_required
def update_cart_item(request, item_id):
    """Update the quantity of a cart item."""
    if request.method == "POST":
        quantity = request.POST.get('quantity')
        cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
        
        # Update the quantity and save
        if quantity and quantity.isdigit() and int(quantity) > 0:
            cart_item.quantity = int(quantity)
            cart_item.save()
        
    return redirect('cart')  # Redirect back to the cart page
