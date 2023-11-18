from django.contrib.sessions.models import Session
from django.db import models

from accounts.models import User
from shop.models import Wine


class Coupons(models.Model):
    coupons = models.CharField(max_length=155)
    date_expiration = models.DateField(format('%Y/%m/%d'))
    percent_discount = models.FloatField()


class Cart(models.Model):
    session = models.ForeignKey(Session, null=True, blank=True, on_delete=models.CASCADE)
    items = models.ManyToManyField('CartItem', null=True, default=None)
    date_generation = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.date_generation)


class CartItem(models.Model):
    cart_items = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Wine, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.pk)


class CheckoutAddress(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.PROTECT, related_name='+')
    session_guest = models.OneToOneField(Session, null=True, blank=True, on_delete=models.CASCADE)
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


class OrderInformation(models.Model):
    date = models.DateTimeField(auto_now=True)

    STATUS_LIST = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('cancel', 'Cancel'),
        ('delivered', 'Delivered')
    )

    status = models.CharField(max_length=255, choices=STATUS_LIST, default=STATUS_LIST[0][0])
    cart_data = models.ForeignKey(Cart, on_delete=models.CASCADE)
    address_data = models.ForeignKey(CheckoutAddress, on_delete=models.CASCADE)
    payment_is = models.BooleanField(default=False)
    user = models.ForeignKey('accounts.User', on_delete=models.PROTECT, null=True)
    payment_method = models.CharField(max_length=255, default=None)

    def __str__(self):
        return f'Order Nr.{self.pk}'

