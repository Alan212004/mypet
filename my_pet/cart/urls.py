from django.urls import path
from . import views 
from .views import update_cart_item

urlpatterns = [
    path('', views.user_cart, name='user_cart'),  # Correct route for viewing the cart
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:item_id>/', update_cart_item, name='update_cart_item'),
]
