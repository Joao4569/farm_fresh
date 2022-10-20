from django import template


register = template.Library()


# For calculating the subtotal
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
