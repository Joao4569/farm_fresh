"""farm_fresh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404

urlpatterns = [
    # Path to Django admin site
    path('admin/', admin.site.urls),

    # Path to Django Allauth URL's
    path('accounts/', include('allauth.urls')),

    # Path to Home app URL's
    path('', include('home.urls')),

    # Path to Products app URL's
    path('products/', include('products.urls')),

    # Path to Shopping cart app URL's
    path('cart/', include('cart.urls')),

    # Path to Checkout app URL's
    path('checkout/', include('checkout.urls')),

    # Path to User profile app URL's
    path('profile/',
         include('user_profiles.urls')),

    # media path
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Path to 404 handler
handler404 = 'farm_fresh.views.handler404'
