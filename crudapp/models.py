from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ShopItem(models.Model):
    itemname = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default='0.00')


    def __str__(self):

        return f'{self.itemname} - {self.price}'

    