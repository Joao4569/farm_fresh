from django.contrib import admin
from .models import Product, Category, Producer, Packaging
# taken directly from Boutique Ado and customised for Farm Fresh


class ProductAdmin(admin.ModelAdmin):
    """This class will extend the built in model admin class and adjust
    how the products information is displayed to the user on the admin
    site for a much better UX"""

    list_display = (
        'name',
        'category',
        'price',
        'producer',
        'image',
        'organic',
        'in_season',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    """This class will extend the built in model admin class and adjust
    how the category information is displayed to the user on the admin
    site for a much better UX"""
    list_display = (
        'friendly_name',
        'name',
    )


class ProducerAdmin(admin.ModelAdmin):
    """This class will extend the built in model admin class and adjust
    how the producer information is displayed to the user on the admin
    site for a much better UX"""

    list_display = (
        'name',
        'image',
    )

    ordering = ('name',)


class PackagingAdmin(admin.ModelAdmin):
    """This class will extend the built in model admin class and adjust
    how the packaging information is displayed to the user on the admin
    site for a much better UX"""

    list_display = (
        'name',
        'packaging_type',
        'weight',
    )

    ordering = ('name',)


# register models and related classes on admin site
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Producer, ProducerAdmin)
admin.site.register(Packaging, PackagingAdmin)
