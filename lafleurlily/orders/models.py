from django.contrib.sessions.models import Session
from django.db import models
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


class Checkout(models.Model):
    cart_information = models.OneToOneField(Cart, on_delete=models.PROTECT)
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

    STATUS_LIST = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('cancel', 'Cancel'),
        ('delivered', 'Delivered')
    )

    status = models.CharField(max_length=255, choices=STATUS_LIST, default=STATUS_LIST[0][0])


