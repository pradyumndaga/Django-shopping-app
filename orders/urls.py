from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.createOrder, name='create_order'),
    path('get-orders', views.getOrders, name='get_orders'),
    path('get-orders-intervals', views.getOrdersInInterval, name='get_orders')
]