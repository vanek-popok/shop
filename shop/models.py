from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    price = models.PositiveIntegerField()
    count = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/')
    rating = models.PositiveSmallIntegerField()
    discount = models.PositiveSmallIntegerField()

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    address = models.TextField()
    phone = models.CharField(max_length=8)
    email = models.CharField(max_length=52, null=True, blank=True)
    koment = models.TextField(null=True, blank=True)
    count = models.PositiveBigIntegerField()
