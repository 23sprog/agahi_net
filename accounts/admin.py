from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as MainUserAdmin
from .forms import CreationUserForm, ChangeUserForm
from django.contrib.auth.models import Group


# Register your models here.

class UserAdmin(MainUserAdmin):
    form = ChangeUserForm
    add_form = CreationUserForm

    list_display = ("email", "last_name", "is_admin", "is_company_admin")
    list_filter = ("email",)

    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

    fieldsets = (
        (None, {"fields": ("email", "username", "first_name", "last_name")}),
        ("جزییات دیگر", {"classes": ("collapse",), "fields": ("is_active", "is_admin", "courses", "company")}),)

    add_fieldsets = ((None, {'fields': ("email", "username", "password1", "password2")}),)
    
    filter_horizontal = ()



admin.site.unregister(Group)
admin.site.register(User, UserAdmin)