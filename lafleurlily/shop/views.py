from django.shortcuts import render, get_object_or_404
from django.views import View
from shop.models import *
from mixins.subscribe_mixin import SubscribePost


class ShopAllProducts(SubscribePost, View):
    template = 'shop/shop.html'
    redirect_page = 'all_products'

    def get(self, request):
        action = request.GET.get('action')
        print('action is = ', action)

        if action == 'search-product':
            return self.search(request)
        elif action == 'ordering':
            return self.ordering(request)

        else:
            all_products = Wine.objects.all()
            return render(request, self.template, {'all_wines': all_products})

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
        print('function ordering is start')
        ordering_by = request.GET.get('ordering-by')
        # paged = request.GET.get('paged', '1')

        if ordering_by == 'popularity':
            products = Wine.objects.order_by('-price')
        elif ordering_by == 'price-up':
            products = Wine.objects.order_by('price')
        elif ordering_by == 'price-low':
            products = Wine.objects.order_by('-price')
        else:
            products = Wine.objects.all()

        return render(request, self.template, {'sort_results': products})


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


