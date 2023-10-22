from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import SingUpForm


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
                    return render(request, self.template, {'msg_superuser': msg_superuser})

                else:
                    return redirect('all_products')

        return render(request, self.template)


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
    template = 'accounts/sing_up.html'

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template)
        else:
            return redirect('login')
