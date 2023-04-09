from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from games.models import Category, Products, PurchaseMethod, Basket
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from common.views import TitleMixin
from django.core.cache import cache


# Create your views here.

class GamesListView(TitleMixin, ListView):
    model = Products
    paginate_by = 6
    template_name = 'games/products.html'
    title = 'Game Store'

    def get_queryset(self):
        queryset = super(GamesListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GamesListView, self).get_context_data()
        context['category'] = Category.objects.all()
        return context


class GamePageView(TitleMixin, DetailView):
    model = Products
    template_name = 'games/gamePage.html'
    title = 'Game Store'

    def get_context_data(self, **kwargs):
        context = super(GamePageView, self).get_context_data()
        games_cache = cache.get('game')
        if not games_cache:
            context['object'] = context['object']
            cache.set('game', context['object'], 30)
        else:
            context['object'] = games_cache
        return context


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
