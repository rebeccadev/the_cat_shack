from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JYWZIIQYqqI4EiS0LZwRXNDH9tCmzQsoPqiGv1VqMF9ObJEln9SNHXzHmJRAn9NgB8YxH6LUVyMvwtC9lYvuB9c006j3p976c',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
