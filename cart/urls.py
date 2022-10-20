from django.urls import path
from . import views

urlpatterns = [
    # Path to view cart page
    path('', views.view_cart, name='view_cart'),
    # Path to add product to cart
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    # Path to adjust product in cart
    path('adjust/<item_id>/', views.adjust_cart, name='adjust_cart'),
    # Path to remove product in cart
    path('remove/<item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
