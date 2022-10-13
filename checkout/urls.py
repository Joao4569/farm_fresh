from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    # Path to checkout page
    path('', views.checkout, name='checkout'),

    # Path to checkout success page
    path('checkout_success/<order_number>',
         views.checkout_success, name='checkout_success'),

    # Path for stripe webhooks
    path('wh/', webhook, name='webhook'),

    # Path for cached checkout data
    path('cache_checkout_data/', views.cache_checkout_data,
         name='cache_checkout_data'),
]
