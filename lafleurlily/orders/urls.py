from django.urls import path
from orders.views import *


urlpatterns = [
    path('cart/', CartPage.as_view(), name='cart'),
    path('pre-checkout/', PreCheckoutPage.as_view(), name='pre_checkout'),
    path('checkout-info/', CheckoutInfo.as_view(), name='checkout_info'),
    path('checkout-payment/', CheckoutPayment.as_view(), name='checkout_payment')
]
