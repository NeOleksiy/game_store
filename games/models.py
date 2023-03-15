from django.db import models


# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=128)

    def __str__(self):
        return self.category


class PurchaseMethod(models.Model):
    purchase_method = models.CharField(max_length=64)

    def __str__(self):
        return self.purchase_method


class Products(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    account_details = models.TextField(null=True, blank=True)
    rental_time = models.CharField(max_length=64, null=True, blank=True)
    key = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT)
    purchaseMethod = models.ManyToManyField(to=PurchaseMethod,
                                            through='purchase'
                                            )

    def __str__(self):
        return self.name


class Slider(models.Model):
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return "image"


class purchase(models.Model):
    name = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    purchaseMethod = models.ForeignKey(to=PurchaseMethod, on_delete=models.CASCADE)
