from django.contrib import admin
from .models import Product, Category, Producer, Packaging

# register model on admin site
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Producer)
admin.site.register(Packaging)
