import stripe
from stripe_api import stripe_config
from django.shortcuts import render, redirect
from django.views import View
from orders.models import *

stripe.api_key = stripe_config.STRIPE_SECRET_KEY
YOUR_DOMAIN = 'http://127.0.0.1:8000'


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        checkout_id = self.kwargs['pk']
        checkout_obj = Checkout.objects.get(pk=checkout_id)

        items = CartItem.objects.filter(cart_items=checkout_obj.cart_information)

        def item_total():
            summ = 0
            for each in items:
                print(each.product.price, each.quantity)
                summ = summ + each.product.price * each.quantity
            return summ
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'total': item_total()

                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )

        return redirect(checkout_session.url, code=303)


class CancelView(View):
    pass


class SuccessfulView(View):
    pass
