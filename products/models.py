from django.db import models
# from django.utils import timezone, datetime


class Products(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    # def __object__(self):
    #     return self

