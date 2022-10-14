from django.urls import path
from . import views

urlpatterns = [

    # Path to profile page
    path('', views.profile, name='profile'),

    # Path for order history
    path('order_history/<order_number>', views.order_history,
         name='order_history'),
]
