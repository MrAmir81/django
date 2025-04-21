from django.db import models# type: ignore
from django.utils.translation import gettext as _ # type: ignore
from django.utils import timezone # type: ignore
from django.contrib.auth.models import User # type: ignore
from ckeditor.fields import RichTextField # type: ignore



class Blog(models.Model):
    title = models.CharField(_("عنوان"),max_length=60)
    description = models.CharField(_("توضیحات"),max_length=100)
    content = RichTextField(_("محتوا"))
    created_at = models.DateTimeField(_("زمان انتشار"), default=timezone.now)
    author = models.ForeignKey(User, verbose_name=_("نویسنده"), on_delete=models.CASCADE)
    image = models.ImageField(_("تصویر"), upload_to="blogs/",blank=True)
    category = models.ForeignKey("Category",related_name="Blog" , verbose_name=_("دسته بندی"), on_delete=models.CASCADE,blank=True , null= True)
    tags = models.ManyToManyField("Tag", verbose_name=_("تگ ها"), related_name="Blogs",blank=True,null=True)

    class Meta:
        verbose_name = 'بلاگ'
        verbose_name_plural = 'بلاگ ها'

    def __str__(self):
        return self.title
    
class Category(models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    slug = models.SlugField(_("عنوان لاتین"))
    published_at = models.DateTimeField(_("تاریخ انتشار"), auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = 'دسته بندی '
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.slug
    
class Tag(models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    slug = models.SlugField(_("عنوان لاتین "))
    published_at = models.DateTimeField(_("تاریخ انتشار‌"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(_("تاریخ بروز رسانی"), auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'

    def __str__(self):
        return self.title
    

class Comments(models.Model):
    blog = models.ForeignKey("blog", verbose_name=_("مقاله"),related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(_("نام کاربر"), max_length=100)
    email = models.EmailField(_("آدرس الکترونیکی"), max_length=254)
    message = models.TextField(_("متن نظر"))
    date = models.DateTimeField(_("تاریخ انتشار"), auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'


    def __str__(self):
        return self.email
