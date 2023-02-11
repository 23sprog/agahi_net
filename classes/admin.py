from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("parent", "name", "slug")
    fields = ["parent", "name", "slug"]
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active",)
    fields = ["name", "is_active", "slug", "img", "category"]
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category")
    fields = ["name", "slug", "desc", "img", "company", "price", "is_active", "category"]
    prepopulated_fields = {"slug": ("name",)}