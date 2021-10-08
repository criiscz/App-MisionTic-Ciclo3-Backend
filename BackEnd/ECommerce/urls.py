from django.urls import path

from .views.UserView import *

urlpatterns = [
    path('users/<int:pk>/<int:id_search>/', UserDetailView.as_view()),
    path('users/create', UserCreateView.as_view()),
    # path('users/s/', UserByNameView.as_view()),
    # path('users/id/<int:pk>', UserById.as_view()),
    # path('account/create', AccountCreateView.as_view())
]
