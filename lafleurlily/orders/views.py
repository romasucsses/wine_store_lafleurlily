from django.shortcuts import render, get_object_or_404
from django.views import View
from orders.models import *


class CartPage(View):
    template = 'orders/cart.html'

    def get(self, request):
        session_key = request.session.session_key
        if session_key is None:  # cart is empty for unauthenticated users
            return render(request, self.template)

        session = Session.objects.get(session_key=session_key)

        try:
            cart = Cart.objects.get(session=session)

        except Cart.DoesNotExist:  # cart is empty for authenticated users
            return render(request, self.template)

        items = CartItem.objects.filter(cart_items=cart)

        def item_total():
            summ = 0
            for each in items:
                print(each.product.price, each.quantity)
                summ = summ + each.product.price * each.quantity
            return float(summ)

        context = {
            'cart': cart,
            'item': items,
            'item_total': item_total()
        }
        return render(request, self.template, context)

    def post(self, request):
        action = request.POST.get('action')
        if action == 'delete-item':
            return self.delete_item(request)

    def delete_item(self, request):
        item_id = request.POST.get('item_id')
        item = CartItem.objects.get(pk=item_id)
        item.delete()
        return self.get(request)


class PreCheckoutPage(View):
    template = 'orders/choose.html'

    def get(self, request):
        return render(request, self.template)


class CheckoutPage(View):
    pass
