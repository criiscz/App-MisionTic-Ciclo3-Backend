from django.urls import path

from .views.OrderView import CreateOrderView, DetailOrderView
from .views.ProductView import AllProductView, CreateProductView
from .views.UserView import *

urlpatterns = [
    path('users/<int:pk>/<int:id_search>/', UserDetailView.as_view()),
    path('users/create', UserCreateView.as_view()),
    # path('users/s/', UserByNameView.as_view()),
    # path('users/id/<int:pk>', UserById.as_view()),
    # path('account/create', AccountCreateView.as_view())
    path('products/', AllProductView.as_view()),
    path('products/create', CreateProductView.as_view()),
    path('orders/create', CreateOrderView.as_view()),
    path('orders/<int:pk>/<int:id_search>', DetailOrderView.as_view())
]
