from django import template
from games.models import Category, Products, purchase, PurchaseMethod

register = template.Library()


@register.simple_tag()
def get_purchaseMethod(name):
    products = Products.objects.all()
    for products in Products:
        lst = Products.objects.get(name=name).purchaseMethod.all()
    return lst
