from django.urls import path
from . import views

urlpatterns = [
    # Path to view cart page
    path('', views.view_cart, name='view_cart'),
    # Path to add product to cart
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
]
