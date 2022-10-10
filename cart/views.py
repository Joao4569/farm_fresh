from django.shortcuts import render


def view_cart(request):
    """ A view to return the shopping cart contents page """

    return render(request, 'cart/cart.html')
