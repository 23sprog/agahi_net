from django.shortcuts import render, redirect
from django.views.generic import View, CreateView
from .forms import CreationUserForm, RegisterUserForm, LoginUserForm
from .models import User
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
# Create your views here.


def index(req):
    return render(req, "index/index.html", {})


    


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

def logout_user(req):
    logout(req)
    return redirect("account:login")
