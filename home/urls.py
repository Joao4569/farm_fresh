from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # Path to home/landing page
]
