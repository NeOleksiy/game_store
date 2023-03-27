
from django.urls import path


from games.views import index, game_page, basket_add, basket_delete, products

app_name = 'games'

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>', products, name='categories_products'),
    path('page/<int:page>', products, name='paginator'),
    path('game_page/<int:product_id>', game_page, name='game_page'),
    path('basket/add/<int:product_id>/<int:purchase_id>', basket_add, name='basket_add'),
    path('basket/delete/<int:basket_id>', basket_delete, name='basket_delete')


]

