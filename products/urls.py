from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.registerProduct, name='product'),
    path('get-products', views.getProducts, name='get_products'),
]