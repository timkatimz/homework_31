from django.db import models


class Ads(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=1000)
    address = models.CharField(max_length=150)
    is_published = models.BooleanField()


class Category(models.Model):
    name = models.CharField(max_length=100)
