from django.urls import path

from .views import *

urlpatterns = [
    path('products', products, name="products"),
    path('product/<id>', product, name="product"),
]