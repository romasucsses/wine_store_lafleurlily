from django.shortcuts import render, redirect
from django.views import View

from mixins.subscribe_mixin import SubscribePost


class HomePage(SubscribePost, View):
    template = 'pages/index.html'
    redirect_page = 'home'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        action = request.POST.get('action')
        if action == "subscribe":
            return self.subscription(request)


class FindNearMe(SubscribePost, View):
    template = 'pages/find_near_me.html'

    def get(self, request):
        return render(request, self.template)

