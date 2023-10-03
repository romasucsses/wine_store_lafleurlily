from django.db import models
from orders.models import Checkout


class Account(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=355)
    name = models.CharField(max_length=155, null=True)
    last_name = models.CharField(max_length=155, null=True)
    display_name = models.CharField(max_length=255, default=username)
    orders = models.ForeignKey(Checkout, on_delete=models.CASCADE)


class ShippingAddress(models.Model):
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


class HistoryOrders(models.Model):
    order = models.ForeignKey(Checkout, on_delete=models.PROTECT)
