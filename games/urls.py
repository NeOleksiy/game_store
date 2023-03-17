
from django.urls import path


from games.views import products

app_name = 'games'

urlpatterns = [
    path('', products, name='index'),

]

