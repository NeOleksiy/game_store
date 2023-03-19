
from django.urls import path


from games.views import index

app_name = 'games'

urlpatterns = [
    path('', index, name='index'),

]

