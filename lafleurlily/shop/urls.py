from django.urls import path

urlpatterns = [
    path('store/', all_products, name='all_products'),
    path('product-category/wines/', wines_category, name='wine_category'),
    path('product-category/sparkling/', sparkling_category, name='sparkling_category'),
    path('product/<slug:wine_slug>/', each_wine_slug, name='each_wine')
]