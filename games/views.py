from django.shortcuts import render, HttpResponseRedirect

from games.models import Category, Products, purchase, PurchaseMethod, Basket


# Create your views here.


def index(request):
    return render(request, "games/index.html")


def game_page(request):
    return render(request, "games/gamePage.html")


def products(request):
    context = {
        'category': Category.objects.all(),
        'products': Products.objects.all(),
        'baskets': Basket.objects.filter(user=request.user)
    }

    return render(request, "games/products.html", context)


def _purchaseMethod(name):
    lst = Products.objects.get(name=name).purchaseMethod.all()
    return lst


def basket_add(request, product_id):
    product = Products.objects.get(id=product_id)
    temp_basket = Basket.objects.filter(user=request.user, product=product)
    if not temp_basket.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        temp_basket.first().quantity += 1
        temp_basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
