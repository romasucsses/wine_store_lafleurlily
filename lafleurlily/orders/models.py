from django.db import models
from shop.models import Wine


class Coupons(models.Model):
    coupons = models.CharField(max_length=155)
    date_expiration = models.DateField(format('%Y/%m/%d'))
    percent_discount = models.FloatField()


class Cart(models.Model):
    product = models.ForeignKey(Wine, on_delete=models.PROTECT)
    date_generation = models.DateField(auto_now=True)

    def all_summ_of_cart(self):
        wine = Wine.objects.all()
        total_sum = 0

        if wine is not None:
            for product in wine:
                total_sum += product.price

        return total_sum

    def __str__(self):
        return self.pk


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


