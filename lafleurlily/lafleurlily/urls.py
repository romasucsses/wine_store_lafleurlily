from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('store/', include('shop.urls')),
    path('order/', include('orders.urls')),
    path('', include('accounts.urls')),
    path('checkout/', include('stripe_api.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
