from django.urls import path

from .views.UserView import UserView

urlpatterns = [
    path('all-users/', UserView.as_view())
]
