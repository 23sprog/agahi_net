from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, UpdateView, TemplateView, DetailView
from .forms import CreationUserForm, RegisterUserForm, LoginUserForm, ProfileUserForm
from .models import User
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .mixins import AdminCompanyMixin
from classes.models import Company, Classes


def index(req):
    return render(req, "index.html", {})


    


class RegisterUserView(View):
    template_name = "registration/register_accounts.html"
    form_class = RegisterUserForm

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.object.create_user(email=cd["email"], username=cd["username"], password=cd["password1"])
            messages.success(request, "شما در سایت ثبت نام شدید برای ورود اقدام کنید", extra_tags="success")
            return redirect("index")
        return render(request, self.template_name, {"form": form})

class LoginUserView(View):
    class_form = LoginUserForm
    template_name = "registration/login_accounts.html"

    def get(self, request):
        return render(request, self.template_name, {"form": self.class_form})
    def post(self, request):
        form = self.class_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd["email"], password=cd["password"])
            if user is not None:
                login(request, user)
                messages.success(request, "به سایت خوش آمدید", extra_tags="success")
                return redirect("index")
            messages.error(request, "گذرواژه یا ایمیل اشتباه است", extra_tags="danger")
            return redirect("account:login")
        return render(request, self.template_name, {"form": form})

@login_required
def logout_user(req):
    logout(req)
    return redirect("account:login")

class ProfileUserView(LoginRequiredMixin, UpdateView):
    template_name = "registration/profile_accounts.html"
    model = User
    form_class = ProfileUserForm
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return User.object.get(pk=self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(ProfileUserView, self).get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs


class CompanyUserView(AdminCompanyMixin, DetailView):
    template_name = "registration/company_accounts.html"
    context_object_name = "company"
    def get_object(self, queryset=None):
        return Company.objects.get(pk=self.request.user.company.pk)

class ClassUserView(TemplateView):
    template_name = "registration/class_accounts.html"
