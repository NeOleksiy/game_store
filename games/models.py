from django.db import models
from users.models import Users


# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=128)

    def __str__(self):
        return self.category


class Developer(models.Model):
    developer = models.CharField(max_length=156)

    def __str__(self):
        return self.developer


class Publisher(models.Model):
    publisher = models.CharField(max_length=156)

    def __str__(self):
        return self.publisher


class PurchaseMethod(models.Model):
    purchase_method = models.CharField(max_length=64)

    def __str__(self):
        return self.purchase_method


class Products(models.Model):
    name = models.CharField(max_length=128)
    rental_price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    account_price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    full_game_price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    account_details = models.TextField(null=True, blank=True)
    rental_time = models.CharField(max_length=64, null=True, blank=True)
    key = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    image_page = models.ImageField(upload_to='page_photo')
    video_link = models.TextField()
    developer = models.ForeignKey(to=Developer, on_delete=models.CASCADE)
    publisher = models.ForeignKey(to=Publisher, on_delete=models.CASCADE)
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


class Basket(models.Model):
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    purchaseMethod = models.ForeignKey(to=purchase, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Пользователь : {self.user.username} | Продукт : {self.product.name}'
