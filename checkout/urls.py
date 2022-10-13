from django.urls import path
from . import views

urlpatterns = [
    # Path to checkout page
    path('', views.checkout, name='checkout'),

    # Path to checkout success page
    path('checkout_success/<order_number>',
         views.checkout_success, name='checkout_success')
]
