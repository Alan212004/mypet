from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('create_order/', views.create_order, name='create_order'),
    path('user_orders/', views.user_orders, name='user_orders'),  # Add this if missing
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
]