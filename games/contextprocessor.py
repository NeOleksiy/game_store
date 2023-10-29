from games.models import Basket, purchase


def basket(request):
    user = request.user
    baskets = Basket.objects.filter(user=user.id)
    quantity_product = lambda product_id, purchase_method_id: \
        Basket.objects.filter(user=user.id,
                              product=product_id,
                              purchaseMethod=purchase_method_id
                              ).first().quantity
    decimal = lambda product_id, purchase_id: \
        purchase.objects.get(name=product_id,
                             purchaseMethod=purchase_id).price * quantity_product(
            product_id, purchase_id)
    context = {'baskets': Basket.objects.filter(user=user.id),
               'total_sum': sum(decimal(basket_g.product, basket_g.purchaseMethod) for basket_g in baskets),
               'total_quantity': sum(basket_g.quantity for basket_g in baskets)}
    return context if user.is_authenticated else []
