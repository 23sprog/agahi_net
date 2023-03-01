from django.http import Http404
from django.shortcuts import redirect

class AdminCompanyMixin():
    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            if request.user.is_admin or request.user.is_company_admin == True:
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect("account:profile")
        else:
            raise Http404("You Can't see this page.")