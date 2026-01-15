from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=6)
    description = models.TextField(default="This is cool!")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.name

# products/models.py

class Wallet(models.Model):
    address = models.CharField(max_length=100, unique=True)
    connected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
