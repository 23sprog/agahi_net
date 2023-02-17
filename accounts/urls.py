from django.urls import path, re_path, include
from django.contrib.auth import views
from .views import *


app_name = "account"

urlpatterns=[
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", LoginUserView.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    # path("logout/", views.LogoutView.as_view(), name="logout"),
]