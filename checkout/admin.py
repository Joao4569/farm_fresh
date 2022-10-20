from django.contrib import admin
from .models import Order, OrderLineItem
# taken directly from Boutique Ado and customised for Farm Fresh


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """ Setup for order admin display to user """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'country',
                       'delivery_cost', 'order_total',
                       'town_or_city', 'grand_total',
                       'canton', 'original_cart', 'stripe_pid',)

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'delivery_cost',
              'order_total', 'grand_total', 'original_cart', 'stripe_pid',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
