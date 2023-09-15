from django.db import models


class EmailSubscription(models.Model):
    email = models.EmailField()


class FindNearMe(models.Model):
    address = models.CharField(max_length=555)
    link_on_googlemaps = models.TextField()


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=455)
    email = models.EmailField()
    message = models.TextField()
