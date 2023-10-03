from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Reviews(models.Model):
    name = models.CharField(max_length=55)
    stars_count = models.IntegerField()
    review = models.TextField()
    product = models.OneToOneField('shop.Wine', on_delete=models.PROTECT, default= None)


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Wine(models.Model):
    name = models.CharField(max_length=355)
    image = models.ImageField(upload_to="img/%Y/%m/%d/")
    price = models.FloatField()
    category = models.ForeignKey('shop.ProductCategory', on_delete=models.PROTECT)
    description = models.TextField(null=True)
    time_added = models.DateField(auto_now=True)
    quanty = models.IntegerField()
    slug = models.SlugField(max_length=455, db_index=True, unique=True, verbose_name='URL')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('each_wine', kwargs={'wine_slug': self.slug})

    def __str__(self):
        return self.name



