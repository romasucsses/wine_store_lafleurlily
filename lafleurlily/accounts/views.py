from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import SingUpForm
from accounts.models import User
import time


class LoginPage(View):
    template = 'accounts/login.html'

    def get(self, request):
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
                    #
                    # def redirect_to_admin():
                    #     time.sleep(3)
                    #     return redirect('admin:index')
                    #
                    # redirect_to_admin()

                else:
                    return redirect('my_account')

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
        pass


class AccountOrders(View):
    template = 'accounts/my_orders.html'

    def get(self, request):
        if request.user.is_authenticated:

            user = request.user
            return render(request, self.template, {'user': user})

        else:
            return redirect('login')


class ViewOrder(View):
    pass


class AccountAddress(View):
    template = 'accounts/my_address.html'

    def get(self, request):
        if request.user.is_authenticated:

            user = request.user
            return render(request, self.template, {'user': user})

        else:
            return redirect('login')


class LogOut(LogoutView):
    next_page = reverse_lazy('login')



