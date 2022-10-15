from django.urls import path
from . import views

urlpatterns = [
    # Path to all products page
    path('', views.all_products, name='products'),

    # Path to product detail page
    path('<int:product_id>/', views.product_detail, name='product_detail'),

    # Path to add product page for superusers
    path('add/', views.add_product, name='add_product'),

    # Path to edit a product page for superusers
    path('edit/<int:product_id/', views.edit_product, name='edit_product'),
]
