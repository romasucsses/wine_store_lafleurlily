from django.db import models


class Coupons(models.Model):
    coupons = models.CharField(max_length=155)


class Checkout(models.Model):
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255)
    street_address_1 = models.TextField()
    street_address_2 = models.TextField(null=True)
    city = models.CharField(max_length=155)
    state = models.CharField(max_length=155)
    zip_code = models.CharField(max_length=155)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    order_notes = models.TextField(default=None, null=True)


