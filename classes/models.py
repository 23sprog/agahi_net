from django.db import models





class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name="آدرس ای پی")


class Categories(models.Model):
    parent = models.ForeignKey("self", blank=True, on_delete=models.SET_NULL, null=True, verbose_name="دسته بندی ارشد")
    name = models.CharField(max_length=40, verbose_name="نام دسته بندی")
    slug = models.SlugField(unique=True, verbose_name="اسلاگ")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=40, verbose_name="نام آموزشگاه")
    img = models.ImageField(upload_to="company_pic/", default="company_pic/default_class.png", verbose_name="عکس")
    is_active = models.BooleanField(verbose_name="در سایت وجود داشته باشد؟؟")
    slug = models.SlugField(unique=True, verbose_name="اسلاگ")
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, related_name="company", verbose_name="دسته بندی")
    desc = models.TextField(default="توضیحات", verbose_name="توضیحات")
    city = models.ForeignKey("City", on_delete=models.SET_NULL, null=True, related_name="company", verbose_name="شهر")
    # company_admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="company", verbose_name="مدیر موسسه")

    class Meta:
        verbose_name = "آموزشگاه"
        verbose_name_plural = "آموشگاه ها"

    def __str__(self):
        return self.name

class Classes(models.Model):
    name = models.CharField(max_length=40, verbose_name="نام دوره")
    slug = models.SlugField(unique=True, verbose_name="اسلاگ")
    desc = models.TextField(verbose_name="توضیحات")
    img = models.ImageField(upload_to="class_pic/", default="class_pic/default_class.png", verbose_name="عکس")
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, related_name="classes", null=True, verbose_name="آموزشگاه")
    price = models.IntegerField(verbose_name="قیمت دوره")
    is_active = models.BooleanField(verbose_name="در سایت وجود داشته باشد؟؟")
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, related_name="classes", verbose_name="دسته بندی")
    views = models.ManyToManyField(IPAddress, blank=True, verbose_name="بازدید")

    class Meta:
        verbose_name = "کلاس"
        verbose_name_plural = "کلاس ها"

    def __str__(self):
        return self.name

    def published(self):
        return self.objects.filter(is_active=True)


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام شهر")
    position = models.PositiveSmallIntegerField(verbose_name="منطقه قرارگیری")

    class Meta:
        verbose_name = "شهر"
        verbose_name_plural = "شهر ها"
        ordering = [
            "position"
        ]

    def __str__(self):
        return self.name