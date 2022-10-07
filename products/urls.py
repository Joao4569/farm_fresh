from django.urls import path
from . import views

urlpatterns = [
    # Path to all products page
    path('', views.all_products, name='products'),
    # Path to product detail page
    path('<product_id>', views.product_detail, name='product_detail'),
]
