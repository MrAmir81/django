from django.db import models #type:ignore
from django.utils.translation import gettext as _ #type:ignore
from ckeditor.fields import RichTextField # type: ignore

class Contact(models.Model):
    name = models.CharField(_("نام"), max_length=50)
    email = models.EmailField(_("ایمیل"), max_length=254)
    message = RichTextField(_("پیام"))

    class Meta:
        verbose_name = "مخاطب"
        verbose_name_plural = "مخاطبان"

    def __str__(self):
        return self.email