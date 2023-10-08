from django.urls import path, re_path
from shop.views import *

urlpatterns = [
    path('', ShopAllProducts.as_view(), name='all_products'),
    path('category/wines/', WineCategory.as_view(), name='wine_category'),
    path('category/sparkling/', SparklingCategory.as_view(), name='sparkling_category'),
    path('<slug:wine_slug>/', Product.as_view(), name='each_wine'),

]
