from django.urls import path
from orders.views import *


urlpatterns = [
    path('cart/', CartPage.as_view(), name='cart'),
    path('pre-checkout/', PreCheckoutPage.as_view(), name='pre_checkout'),
    path('checkout-as-guest/', CheckoutAsGuest.as_view(), name='checkout_as_guest'),
    path('checkout-as-user/', CheckoutAsUser.as_view(), name='checkout_as_user')
]
