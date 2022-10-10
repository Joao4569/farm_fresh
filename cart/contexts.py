from decimal import Decimal
from django.conf import settings


def cart_contents(request):
    """ This will use the request as a parameter and instead of returning a
    template, this function will return a dictionary called context which
    will contain the shopping cart contents so they can be accessed by
    any template throughout the site. i.e. A context processor for the
    cart's contents """

    cart_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        """ I used the decimal function since this is a financial transaction
        and using float is susceptible to rounding errors. """
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
