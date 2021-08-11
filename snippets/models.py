# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    def __str__(self):
        return self.first_name

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Product(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)
