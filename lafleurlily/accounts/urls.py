from django.urls import path
from accounts.views import *

urlpatterns = [
    path('sing-up/', SingUpPage.as_view(), name='sing_up'),
    path('login/', LoginPage.as_view(), name='login'),
    path('my-account/', MyAccountPage.as_view(), name='my_account'),
    path('my-account/orders/', AccountOrders.as_view(), name='account_orders'),
    path('my-account/address/', AccountAddress.as_view(), name='account_address'),
    path('my-account/logout/', LogOut.as_view(), name='logout'),
    path('my-account/orders/view-order/', ViewOrder.as_view(), name='view-order')
]