from django.urls import path
from accounts.views import *

urlpatterns = [

    path('sing-up/', SingUpPage.as_view(), name='sing_up'),
    path('login/', LoginPage.as_view(), name='login'),
    path('my-account/', MyAccountPage.as_view(), name='my_account'),
    path('my-account/orders/', AccountOrders.as_view(), name='account_orders'),
    path('my-account/orders/view-order/<int:pk>/', ViewOrder.as_view(), name='view_order'),
    path('my-account/address/', AccountAddress.as_view(), name='account_address'),
    path('my-account/address/add-new/', AccountAddNewAddress.as_view(), name='add_new_address'),
    path('my-account/address/edit-view/', EditAccountAddress.as_view(), name='edit_address'),
    path('my-account/logout/', LogOut.as_view(), name='logout'),

]
