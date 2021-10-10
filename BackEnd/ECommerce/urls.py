from django.urls import path

from .views.OrderView import CreateOrderView, DetailOrderView, UpdateOrderView
from .views.ProductView import AllProductView, CreateProductView, SearchByIdProductView, SearchByNameProductView
from .views.UserView import *

urlpatterns = [
    path('users/<int:id_search>', UserDetailView.as_view()),
    path('users/create', UserCreateView.as_view()),
    path('users/current/', UserById.as_view()),

    path('products', AllProductView.as_view()),
    path('products/', SearchByNameProductView.as_view()),
    path('products/<int:product_id>', SearchByIdProductView.as_view()),
    path('products/create', CreateProductView.as_view()),

    path('orders/create', CreateOrderView.as_view()),
    path('orders/<int:pk>', DetailOrderView.as_view()),
    path('orders/update/status/<int:pk>', UpdateOrderView.as_view())
]
