from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=128)

    def __str__(self):
        return self.category


class Products(models.Model):
    name = models.CharField(max_length=128)
    purchase_method = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    account_details = models.TextField(null=True, blank=True)
    rental_time = models.DateField(null=True, blank=True)
    key = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to='games_images')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

