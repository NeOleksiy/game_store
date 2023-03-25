from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from games.models import Category, Products, purchase, PurchaseMethod, Basket


# Create your views here.


def index(request):
    return render(request, "games/index.html")


def game_page(request, product_id):
    context = {
        'product_page': Products.objects.get(id=product_id)
    }
    return render(request, "games/gamePage.html", context)


def products(request):
    context = {
        'category': Category.objects.all(),
        'products': Products.objects.all(),
    }

    return render(request, "games/products.html", context)


@login_required
def basket_add(request, product_id, purchase_id):
    product = Products.objects.get(id=product_id)
    purchase_method = PurchaseMethod.objects.get(id=purchase_id)
    temp_basket = Basket.objects.filter(user=request.user, product=product, purchaseMethod=purchase_method)
    if not temp_basket.exists():
        Basket.objects.create(user=request.user, product=product, purchaseMethod=purchase_method, quantity=1)
    else:
        basket = temp_basket.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_delete(request, basket_id):
    temp_basket = Basket.objects.get(user=request.user, id=basket_id)
    if temp_basket.quantity > 1:
        temp_basket.quantity -= 1
        temp_basket.save()
    else:
        Basket.objects.get(user=request.user, id=basket_id).delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
