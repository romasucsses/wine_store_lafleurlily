from django.urls import path
from accounts.views import *

urlpatterns = [
    path('my-account/', MyAccountPage.as_view(), name='my_account'),
    path('sing-up/', SingUpPage.as_view(), name='sing_up'),
    path('login/', LoginPage.as_view(), name='login'),
    #path('my-account/orders/', account_orders, name='account_orders'),
    #path('my-account/edit-address/', account_address, name='account_address'),
    #path('my-account/edit-account/', account_details, name='account_details'),
    #path('my-account/logout/', logout, name='logout')
]