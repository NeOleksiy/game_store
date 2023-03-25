from django import template
from games.models import Category, Products, purchase, PurchaseMethod

register = template.Library()


@register.simple_tag()
def get_purchaseMethod(name):
    lst = Products.objects.get(name=name).purchaseMethod.all()
    return lst


@register.simple_tag()
def get_price(product_id, purchase_id):
    return purchase.objects.get(name=product_id, purchaseMethod=purchase_id).price


@register.simple_tag()
def get_sum_price(product_id, purchase_id, quantity):
    return purchase.objects.get(name=product_id, purchaseMethod=purchase_id).price*quantity


@register.simple_tag()
def min_price(product_id):
    id_method = PurchaseMethod.objects.all()[0].id
    return purchase.objects.get(name=product_id, purchaseMethod=id_method).price
