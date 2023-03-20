
from django.urls import path


from games.views import index, game_page

app_name = 'games'

urlpatterns = [
    path('', index, name='index'),
    path('game_page/', game_page, name='game_page')

]

