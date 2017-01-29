from django.db import models
import uuid
import os
from cloudinary.models import CloudinaryField
import moneyed
from djmoney.models.fields import MoneyField

# Create your models here.
def upload(file, **options):
    print(file)

def scramble_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(), extension)

class Shop(models.Model):

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product_logo = CloudinaryField('CategoryImage')

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.product_logo.path):
            os.remove(self.product_logo.path)

        super(Shop, self).delete(*args, **kwargs)

    def __str__(self):
        return self.title

class Product(models.Model):

    shop = models.ForeignKey(Shop, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    long_description = models.TextField()
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='GBP')
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product_logo = CloudinaryField('ProductImage')

    def __str__(self):
        return self.title + ' - ' + self.short_description

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.product_logo.path):
            os.remove(self.product_logo.path)

        super(Shop, self).delete(*args, **kwargs)

class Contact(models.Model):
    openingTimes = models.CharField(max_length=300)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=400)
    road = models.CharField(max_length=200)
    town = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    postcode = models.CharField(max_length=50)

    def __str__(self):
        return self.openingTimes

class About(models.Model):
    pass