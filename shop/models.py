from django.db import models
import uuid

# Create your models here.

def scramble_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(), extension)

class Shop(models.Model):

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product_logo = models.FileField('Product Images', upload_to=scramble_filename)

    def __str__(self):
        return self.title

class Product(models.Model):

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=5)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product_logo = models.FileField('Product Images', upload_to=scramble_filename)

    def __str__(self):
        return self.title + ' - ' + self.description