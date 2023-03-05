from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "games/index.html")


def products(request):
    return render(request, "games/products.html")
