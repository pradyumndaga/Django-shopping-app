import datetime  
from django.db import models

from products.models import Products

# Create your models here.
class Orders(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(default= datetime.datetime.now())
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)

    # def order_in_interval(self, days):
    #     return self.purchase_date >= timezone.now() - datetime.timedelta(days=days)