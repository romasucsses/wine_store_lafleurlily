from django.db import models


class Wine(models.Model):
    name = models.CharField(max_length=355)
    image = models.ImageField(upload_to="img/%Y/%m/%d/")
    price = models.IntegerField()
    category = models.CharField(max_length=355)
    description = models.TextField(null=True)
    time_added = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Reviews(models.Model):
    review = models.TextField()


