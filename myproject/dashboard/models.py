from django.db import models
from django.contrib.auth.models import User

import logging
from djangoHexadecimal.fields import HexadecimalField

#create tuple category
CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
    )
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Product'
    def __str__(self):
        return f'{self.name}--{self.quantity}'

class Order(models.Model):
        product = models.ForeignKey(Product, on_delete = models.CASCADE)
        staff = models.ForeignKey(User, models.CASCADE, null=True)
        order_quantity = models.PositiveIntegerField(null=True)
        date = models.DateTimeField(auto_now_add=True)

        class Meta:
            verbose_name_plural = 'Order'

        def __str__(self):
            return f'{self.product} ordered by {self.staff.username}'


class Result(models.Model):
    id = models.CharField(max_length=300, primary_key=True)
    a = models.PositiveIntegerField(null=True)
    b = models.PositiveIntegerField(null=True)
    res = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Result'

    def __str__(self):
        return f'{self.id} --{self.a} --{self.b}--{self.res}'



class Item(models.Model):
    result = models.ForeignKey(Result, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()
    def __str__(self):
        return self.text

