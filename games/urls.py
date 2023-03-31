
from django.urls import path


from games.views import basket_add, basket_delete, GamesListView, GamePageView

app_name = 'games'

urlpatterns = [
    path('category/<int:category_id>', GamesListView.as_view(), name='categories_products'),
    path('page/<int:page>', GamesListView.as_view(), name='paginator'),
    path('game_page/<int:pk>', GamePageView.as_view(), name='game_page'),
    path('basket/add/<int:product_id>/<int:purchase_id>', basket_add, name='basket_add'),
    path('basket/delete/<int:basket_id>', basket_delete, name='basket_delete')


]

