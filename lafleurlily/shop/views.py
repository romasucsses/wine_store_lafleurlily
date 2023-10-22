from django.shortcuts import render, get_object_or_404
from django.views import View
from shop.models import *
from mixins.subscribe_mixin import SubscribePost


class BaseFunctions(SubscribePost):
    filter_category = None

    best_sellers_prod = Wine.objects.order_by('-price')[:4]
    context = {'best_sellers': best_sellers_prod}

    def get(self, request):

        action = request.GET.get('action')

        if action == 'search-product':
            return self.search_product(request)
        elif action == 'ordering':
            return self.ordering(request)

        else:
            if self.filter_category:
                all_products = Wine.objects.filter(category=self.filter_category)
            else:
                all_products = Wine.objects.all()

            self.context.update({'all_wines': all_products})
            return render(request=request, template_name=self.template, context=self.context)

    def search_product(self, request):
        query = request.GET.get('query')
        if query and query is not None:
            if self.filter_category:
                products = Wine.objects.filter(name__icontains=query, category=self.filter_category)
            else:
                products = Wine.objects.filter(name__icontains=query)

        else:
            if self.filter_category:
                products = Wine.objects.filter(category=self.filter_category)
            else:
                products = Wine.objects.all()

        self.context.update({'all_wines': products})
        return render(request, self.template, self.context)

    def ordering(self, request):
        ordering_by = request.GET.get('ordering-by')
        if self.filter_category:
            products = Wine.objects.filter(category=self.filter_category)
        else:
            products = Wine.objects.all()

        if ordering_by == 'popularity':
            products = products.order_by('-price')
        elif ordering_by == 'price-up':
            products = products.order_by('price')
        elif ordering_by == 'price-low':
            products = products.order_by('-price')

        self.context.update({'all_wines': products})

        return render(request, self.template, self.context)


class ShopAllProducts(BaseFunctions, View):
    template = 'shop/shop.html'
    redirect_page = 'all_products'


class Product(SubscribePost, View):
    template = 'shop/product.html'
    model = Wine

    def get(self, request, wine_slug):
        product = get_object_or_404(self.model, slug= wine_slug)
        context = {'wine': product}
        return render(request, self.template, context=context)

    def post(self, request):
        pass


class WineCategory(BaseFunctions, View):
    template = 'shop/wine.html'
    filter_category = 1


class SparklingCategory(BaseFunctions, View):
    template = 'shop/sparkling.html'
    filter_category = 2



