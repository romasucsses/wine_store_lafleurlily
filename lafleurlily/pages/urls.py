from django.urls import path
from pages.views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', our_story, name='about_us'),
    path('near_me/', find_near_me, name='stores_near_me'),
    path('contact-us/', contact_us, name='contact_us'),
]