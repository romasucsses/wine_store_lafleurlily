from django.urls import path
from pages.views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('about/', AboutUs.as_view(), name='about_us'),
    path('near_me/', FindNearStore.as_view(), name='find_near_me'),
    path('contact-us/', ContactUs.as_view(), name='contact_us'),
]