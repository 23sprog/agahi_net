from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from django.shortcuts import get_object_or_404


# Create your views here.

class CompanyViewView(ListView):
    paginate_by = 5
    model = Company
    template_name = "classes-templates/company-view.html"
    context_object_name = "companies"

class CompanyDetailView(DetailView):
    template_name = "classes-templates/company-detail.html"
    model = Company

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"classes": Classes.objects.filter(company=company, is_active=True)})
        return context

    def get_object(self):
        global company
        company = get_object_or_404(Company, pk=self.kwargs["id"], slug=self.kwargs["slug"], is_active=True)
        return company

class CompanyAboutView(DetailView):
    template_name = "classes-templates/company-about.html"
    context_object_name = "company"
    model = Company

    def get_object(self):
        return get_object_or_404(Company, pk=self.kwargs["id"], slug=self.kwargs["slug"])

class ClassDetailView(DetailView):
    model = Classes
    template_name = "classes-templates/class_detail.html"

    def get_object(self):
        return get_object_or_404(Classes, pk=self.kwargs["id"], slug=self.kwargs["slug"])
