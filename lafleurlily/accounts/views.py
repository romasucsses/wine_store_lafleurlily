from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import *
from accounts.models import User
from orders.models import *


class LoginPage(View):
    template = 'accounts/login.html'
    next = None

    def get(self, request):
        redirect_url = request.GET.get('redirect_url', None)
        self.next = redirect_url
        return render(request, self.template)

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        msg_superuser = False
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                if user.is_superuser or user.is_staff:
                    msg_superuser = True

                else:
                    if self.next is None:
                        self.next = 'my_account'
                    return redirect(self.next)

        return render(request, self.template, {'msg_superuser': msg_superuser})


class SingUpPage(View):
    template = 'accounts/sing_up.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        form = SingUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')

        return render(request, self.template)


class MyAccountPage(View):
    template = 'accounts/my_account.html'

    def get(self, request):
        if request.user.is_authenticated:

            user = request.user
            return render(request, self.template, {'user': user})

        else:
            return redirect('login')

    def post(self, request):
        action = request.POST.get('action')
        if action == 'save-changes':
            return self.update_account(request)

        return self.get(request)

    def update_account(self, request):
        user = request.user
        form = UpdateUserInfoForm(request.POST, instance=user)

        if user is not None:
            if form.is_valid():
                form.save()
                return redirect('my_account')

        return self.get(request)


class AccountOrders(View):
    template = 'accounts/my_orders.html'

    def get(self, request):
        if request.user.is_authenticated:
            orders = OrderInformation.objects.filter(user=request.user)
            print(orders)

            if not orders:
                print('orders is not')
                return render(request, self.template, {'orders': orders})

            def item_total(number=0):
                summ = 0

                items = CartItem.objects.filter(cart_items=orders[number].cart_data)
                print('items', items)
                for each in items:
                    print('each', each)
                    summ += each.product.price * each.quantity
                return float(summ)

            item_totals = [item_total(i) for i in range(len(orders))]

            orders_with_totals = zip(orders, item_totals)
            return render(request, self.template, {'orders': orders, 'orders_with_totals': orders_with_totals})

        else:
            return redirect('login')


class ViewOrder(View):
    template = 'accounts/view_order.html'

    def get(self, request, pk):
        if request.user.is_authenticated:
            order = OrderInformation.objects.get(pk=pk)
            items = CartItem.objects.filter(cart_items=order.cart_data)

            def item_total():
                summ = 0
                for each in items:
                    summ += each.product.price * each.quantity
                return float(summ)

            return render(request, self.template, {'order': order, 'items': items, 'item_total': item_total()})


class AccountAddress(View):
    template = 'accounts/my_address.html'

    def get(self, request):
        if request.user.is_authenticated:

            user = request.user
            return render(request, self.template, {'user': user})

        else:
            return redirect('login')


class EditAccountAddress(View):
    template = "accounts/edit_shipping_address.html"

    def get(self, request):
        user = request.user
        if user.user_shipping_address is None:
            return redirect('add_new_address')
        else:
            return render(request, self.template, {'user': user})

    def post(self, request):
        form = AddCheckoutAddressForm(request.POST)
        user = request.user
        if user.user_shipping_address is not None:
            if form.is_valid():
                address = user.user_shipping_address

                address.first_name = form.cleaned_data['first_name']
                address.last_name = form.cleaned_data['last_name']
                address.company_name = form.cleaned_data['company_name']
                address.country = form.cleaned_data['country']
                address.street_address_1 = form.cleaned_data['street_address_1']
                address.street_address_2 = form.cleaned_data['street_address_2']
                address.city = form.cleaned_data['city']
                address.state = form.cleaned_data['state']
                address.zip_code = form.cleaned_data['zip_code']
                address.phone = form.cleaned_data['phone']
                address.email = form.cleaned_data['email']

                address.save()

                return redirect('account_address')
        else:
            return redirect('add_new_address')

        return self.get(request)


class AccountAddNewAddress(View):
    template = 'accounts/add_shipping_address.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        form = AddCheckoutAddressForm(request.POST)
        user = request.user
        if form.is_valid():
            if user.user_shipping_address is not None:
                user.user_shipping_address = None
                user.save()
                CheckoutAddress.objects.get(user=user).delete()

            address = form.save(commit=False)
            address.user = user
            address.save()

            user.user_shipping_address = address  # CheckoutAddress.objects.get(user=user_update)
            user.save()

            return redirect('account_address')

        return self.get(request)


class LogOut(LogoutView):
    next_page = reverse_lazy('login')



