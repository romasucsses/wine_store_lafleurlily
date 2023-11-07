from django.urls import path
from stripe_api.views import *


urlpatterns = [
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-stripe-checkout'),
    path('cancel/', CancelView.as_view(), name='cancel-checkout'),
    path('successful/', SuccessfulView.as_view(), name='successful-checkout')
]
