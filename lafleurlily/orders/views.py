from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from orders.models import *
from orders.forms import CheckoutInfoForm
from newsletter.to_admin_sender import *


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


class CheckoutAsGuest(View):
    template = 'orders/checkout_as_guest.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        form = CheckoutInfoForm(request.POST)

        session_key = request.session.session_key
        session = Session.objects.get(session_key=session_key)

        if form.is_valid():
            checkout_info = form.save(commit=False)
            checkout_info.session_guest = session  # Associate with existing session
            checkout_info.save()

            cart_information = get_object_or_404(Cart, session=session)
            order_info = OrderInformation.objects.create(
                cart_data=cart_information,
                address_data=CheckoutAddress.objects.get(session_guest=session)
            )
            new_order_without_payment()

            action = request.POST.get('action')

            if action == 'pay-with-card':
                return redirect('create-stripe-checkout')
            elif action == 'pay-with-paypal':
                pass
        else:
            return render(request, self.template, {'form': form})


class CheckoutAsUser(View):
    template = 'orders/checkout_as_login.html'

    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            return render(request, self.template, {'user': user})
        else:
            return redirect('pre_checkout')

    def post(self, request):
        session_key = request.session.session_key
        session = Session.objects.get(session_key=session_key)
        action = request.POST.get('action')

        cart_information = get_object_or_404(Cart, session=session)
        order_info = OrderInformation.objects.create(
            cart_data=cart_information,
            address_data=CheckoutAddress.objects.get(user=request.user),
            user=request.user,
            payment_method=action
        )

        new_order_without_payment()

        if action == 'pay-with-card':
            return redirect('create-stripe-checkout')
        elif action == 'pay-with-paypal':
            pass

        return self.get(request)
