from django.urls import path
from orders.views import *


urlpatterns = [
    path('cart/', CartPage.as_view(), name='cart'),
    path('checkout/', CheckoutPage.as_view(), name='checkout'),
    path('pre-checkout/', PreCheckoutPage.as_view(), name='pre_checkout')
]