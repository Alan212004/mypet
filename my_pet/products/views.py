from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()  # Assuming you have a Product model
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product_detail.html', {'product': product})
