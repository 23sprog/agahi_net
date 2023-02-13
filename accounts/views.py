from django.shortcuts import render
from django.views.generic import View, CreateView
from .forms import CreationUserForm
from .models import User
# Create your views here.


def index(req):
    return render(req, "index/index.html", {})

class LoginView(View):
    def get(self, request):
        return render(request, "registration/login.html", {})

    def post(self, request):
        return render(request, "registration/login.html", {})
    


class RegisterUserView(View):
    template_name = "registration/register_accounts.html"
    form_class = CreationUserForm

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})
