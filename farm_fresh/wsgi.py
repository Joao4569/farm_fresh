"""
WSGI config for farm_fresh project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
# taken directly from Boutique Ado and customised for Farm Fresh

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farm_fresh.settings')

application = get_wsgi_application()
