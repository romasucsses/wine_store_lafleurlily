from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from orders.models import Cart, CartItem
from shop.forms import AddReviewForm
from shop.models import *
from mixins.subscribe_mixin import SubscribePost
from django.contrib.sessions.models import Session


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


class Product(View): #SubscribePost,
    template = 'shop/product.html'
    model = Wine

    def get(self, request, wine_slug):
        product = get_object_or_404(self.model, slug=wine_slug)
        reviews = Reviews.objects.filter(product=product)
        all_products = Wine.objects.all()
        context = {'wine': product, 'reviews': reviews, 'all_reviews': reviews.count(), 'all_products': all_products[:3]}

        return render(request, self.template, context=context)

    def post(self, request, wine_slug):
        action = request.POST.get('action')
        if action == 'add_to_cart':
            return self.add_to_cart(request, wine_slug)
        elif action == 'add-review':
            return self.add_review(request, wine_slug)

    def add_review(self, request, wine_slug):
        form = AddReviewForm(request.POST)
        product = get_object_or_404(self.model, slug=wine_slug)

        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()

        return self.get(request, wine_slug=wine_slug)

    def add_to_cart(self, request, wine_slug):

        if not request.user.is_authenticated:
            if not request.session.session_key:
                request.session.create()

        else:
            if not request.session.session_key:
                request.session.create()

        session_key = request.session.session_key

        session = get_object_or_404(Session, session_key=session_key)
        product = Wine.objects.get(slug=wine_slug)

        cart, created = Cart.objects.get_or_create(session=session)
        cart_item, item_created = CartItem.objects.get_or_create(cart_items=cart, product=product)

        if cart_item:
            cart_item.quantity += 1
            cart_item.save()

        return redirect('cart')



class WineCategory(BaseFunctions, View):
    template = 'shop/wine.html'
    filter_category = 1


class SparklingCategory(BaseFunctions, View):
    template = 'shop/sparkling.html'
    filter_category = 2



