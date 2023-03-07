from django.contrib import admin
from games.models import Category, Products, PurchaseMethod, Slider

# Register your models here.


admin.site.register(Products)
admin.site.register(Category)
admin.site.register(PurchaseMethod)
admin.site.register(Slider)
