from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return f'{self.name}'


class Producer(models.Model):
    name = models.CharField(max_length=60, unique=True)
    address = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=300)


class Product(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=300)
    price = models.IntegerField(default=0)
    availability = models.BooleanField(default=True)
    producer = models.ForeignKey(Producer, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
