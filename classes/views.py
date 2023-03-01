from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import User
from django.shortcuts import redirect

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
        classes = get_object_or_404(Classes, pk=self.kwargs["id"], slug=self.kwargs["slug"])
        if self.request.user.ip_address not in classes.views.all():
            classes.views.add(self.request.user.ip_address)
        return classes

class BuyClassView(LoginRequiredMixin, View):
    http_method_names = ("post",)
    def post(self, request):
        kwargs = request.POST
        classes = get_object_or_404(Classes, pk=kwargs.get("pk"), slug=kwargs.get("slug"))
        user = User.object.get(pk=request.user.pk)
        user.courses.add(classes)
        return redirect("classes:class_detail", classes.id, classes.slug)