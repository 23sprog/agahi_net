from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from classes.models import Classes, Company
from .managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, verbose_name="ایمیل")
    username = models.CharField(max_length=255, unique=True,verbose_name="نام کاربری")
    first_name = models.CharField(max_length=200, verbose_name="نام")
    last_name = models.CharField(max_length=200, verbose_name="نام خانوادگی")
    is_active = models.BooleanField(default=True, verbose_name="کاربر فعال")
    is_admin = models.BooleanField(default=False, verbose_name="وضعیت کارمندی")
    courses = models.ManyToManyField(Classes, blank=True, verbose_name="دوره ها")
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, verbose_name="موسسه")

    def is_company_admin(self):
        if self.company:
            return True
        else:
            return False
    is_company_admin.boolean = True
    is_company_admin.short_description = "مدیر موسسه"

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    object = UserManager()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def has_perm(self, perm, obj=False):
        return True
    
    def has_module_perms(self, app_label):
        return True


    @property
    def is_staff(self):
        return self.is_admin
    
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
    

