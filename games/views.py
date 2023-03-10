from django.shortcuts import render

from games.models import Category, Products


# Create your views here.


def index(request):
    return render(request, "games/index.html")


def products(request):
    context = {
        'category': Category.objects.all(),
        'products': Products.objects.all(),

    }
    return render(request, "games/products.html", context)
