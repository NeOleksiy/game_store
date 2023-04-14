from django.urls import path
from order.views import OrderCreateView, Success, Cancel
from django.contrib.auth.decorators import login_required

app_name = 'orders'

urlpatterns = [
    path('order_create/', login_required(OrderCreateView.as_view()), name='order_create'),
    path('order_succes/', Success.as_view(), name='order_success'),
    path('order_cancel/', Cancel.as_view(), name='order_cancel'),
]
