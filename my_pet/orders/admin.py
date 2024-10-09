# orders/admin.py

from django.contrib import admin
from .models import Product, Category  # Import your models

# Register your models with the admin site
admin.site.register(Product)  # This makes the Product model available in the admin
admin.site.register(Category)  # This makes the Category model available in the admin

