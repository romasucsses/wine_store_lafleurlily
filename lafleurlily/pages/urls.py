from django.urls import path
from pages.views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    # path('about/', our_story, name='about_us'),
    path('near_me/', FindNearMe.as_view(), name='find_near_me'),
    # path('contact-us/', contact_us, name='contact_us'),
]