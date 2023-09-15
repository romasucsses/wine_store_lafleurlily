from django.db import models


class Reviews(models.Model):
    name = models.CharField(max_length=55)
    stars_count = models.IntegerField()
    review = models.TextField()


class Wine(models.Model):
    name = models.CharField(max_length=355)
    image = models.ImageField(upload_to="img/%Y/%m/%d/")
    price = models.IntegerField()
    category = models.CharField(max_length=355)
    description = models.TextField(null=True)
    time_added = models.DateField(auto_now=True)
    quanty = models.IntegerField()
    reviwes = models.ForeignKey(to='Reviews', on_delete=models.PROTECT)

    def __str__(self):
        return self.name
