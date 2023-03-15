from django.shortcuts import render


from games.models import Category, Products, purchase, PurchaseMethod


# Create your views here.


def index(request):
    return render(request, "games/index.html")


def products(request):
    context = {
        'category': Category.objects.all(),
        'products': Products.objects.all(),
        # 'purchase': Products.objects.get().purchaseMethod.all()
    }

    return render(request, "games/products.html", context)



