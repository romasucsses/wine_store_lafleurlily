from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View

from pages.forms import SendMSGForm
from shop.models import *
from pages.models import *

from mixins.subscribe_mixin import SubscribePost



class HomePage(SubscribePost, View):
    template = 'pages/index.html'
    redirect_page = 'home'
    products = Wine.objects.all()[:8]

    def get(self, request):
        return render(request, self.template, context={'all_wines': self.products})


class FindNearStore(SubscribePost, View):
    template = 'pages/find_near_me.html'
    redirect_page = 'find_near_me'

    def get(self, request):
        action = request.GET.get('action')
        print('action',action)

        if action == 'search_stores':
            return self.search_store(request)
        elif action == 'show_all':
            return self.show_all(request)
        else:
            return self.show_all(request)

    def show_all(self, request):
        all_stores = FindNearMe.objects.all()
        context = {'all_stores': all_stores}
        return render(request, self.template, context=context)

    def search_store(self, request):
        print('search is started')
        address = request.GET.get('query')
        if address and address is not None:
            print('address', address)
            print('address is true and note none, is started')
            stores = FindNearMe.objects.filter(address__icontains=address)
            return render(request, self.template, {'search_results': stores})
        else:
            return self.show_all(request)


class AboutUs(SubscribePost, View):
    template = 'pages/about_us.html'
    redirect_page = 'about_us'

    def get(self, request):
        return render(request, self.template)


class ContactUs(SubscribePost, View):
    template = 'pages/contact_us.html'
    redirect_page = 'contact_us'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        action = request.POST.get('action')
        if action == "send-msg":
            return self.send_msg(request)

    def send_msg(self, request):
        form = SendMSGForm(request.POST)
        if form.is_valid():
            form.save()

        return self.get(request)









