from django.shortcuts import render
from django.views import View


class LoginPage(View):
    template = 'accounts/login.html'

    def get(self, request):
        return render(request, self.template)
