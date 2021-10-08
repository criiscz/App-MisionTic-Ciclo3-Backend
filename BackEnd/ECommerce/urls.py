from django.urls import path, re_path

from .views.UserView import *

urlpatterns = [
    path('users/', UserView.as_view()),
    path('users/s/', UserDetail.as_view())
]
