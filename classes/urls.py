from django.urls import path
from .views import *

app_name = "classes"

urlpatterns = [
    path("company/", CompanyViewView.as_view(), name="company_view"),
    path("company/detail/<int:id>/<slug:slug>/", CompanyDetailView.as_view(), name="company_detail"),
    path("company/detail/about/<int:id>/<slug:slug>/", CompanyAboutView.as_view(), name="company_about"),
    path("class/detail/<int:id>/<slug:slug>/", ClassDetailView.as_view(), name="class_detail"),
]