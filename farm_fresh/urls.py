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

urlpatterns = [
    path('admin/', admin.site.urls),  # Path to Django admin site
    path('accounts/', include('allauth.urls')),  # Path to Django Allauth URL's
    path('', include('home.urls')),  # Path to Home app URL's
    path('products/', include('products.urls')),  # Path to Products app URL's
    path('cart/', include('cart.urls')),  # Path to Products app URL's
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # media path
