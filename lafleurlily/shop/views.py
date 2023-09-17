from django.shortcuts import render, get_object_or_404
from django.views import View
from shop.models import *
from mixins.subscribe_mixin import SubscribePost


class ShopAllProducts(SubscribePost, View):
    template = 'shop/shop.html'
    redirect_page = 'all_products'

    def get(self, request):
        action = request.POST.get('action')
        if action == 'search-product':
            return self.search(request)
        elif action == 'ordering':
            return self.ordering(request)
        else:
            return render(request, self.template)

    def post(self, request):
        action = request.POST.get('action')
        if action == "subscribe":
            return self.subscription(request)

    def search(self, request):
        query = request.GET.get('query')
        if query:
            products = Wine.objects.filter(name__icontains=query)

        else:
            products = Wine.objects.all()

        return render(request, self.template, {'wine': products})

    def ordering(self, request):
        ordering_by = request.GET.get('ordering-by', 'menu')
        paged = request.GET.get('paged', '1')

        if ordering_by == 'popularity':
            products = Wine.objects.order_by('price')
        elif ordering_by == 'price-up':
            products = Wine.objects.order_by('price')
        elif ordering_by == 'price-low':
            products = Wine.objects.order_by('-price')
        else:
            products = Wine.objects.all()

        context = {'products': products}

        return render(request, self.template, context)


class Product(SubscribePost, View):
    template = 'shop/product.html'
    model = Wine

    def get(self, request, wine_slug):
        product = get_object_or_404(self.model, slug= wine_slug)
        context = {'wine': product}
        return render(request, self.template, context=context)

    def post(self, request):
        pass


class WineCategory(SubscribePost, View):
    template = 'shop/wine.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        pass


class SparklingCategory(SubscribePost, View):
    template = 'shop/sparkling.html'

    def get(self, request):
        return render(request, self.template)


