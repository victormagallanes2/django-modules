from django.db import models
from django.db.models import SET_NULL


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='category/', blank=True)

    def __str__(self):
        return self.name
    
class Products(models.Model):
    name = models.CharField(max_length=50)
    # quantity = models.DecimalField(max_digits=100,default='0', decimal_places=2, null=True, blank=True)
    # price = models.DecimalField(max_digits=100, default='0', decimal_places=2, blank=True)
    description = models.TextField(max_length=250, blank=True)
    picture = models.ImageField(upload_to='products/', blank=True)
    category = models.ManyToManyField(Category)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name