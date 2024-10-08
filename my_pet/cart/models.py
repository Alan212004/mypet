from django.contrib.auth.models import User
from django.db import models
from products.models import Product

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Cart of {self.user.username}'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE, null=True)  # Allow null values
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # Allow null values

    def __str__(self):
        return f'{self.quantity} of {self.product.name}'

