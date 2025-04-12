from django.db import models # type:ignore
from django.utils.translation import gettext as _ # type:ignore

class Reservation(models.Model):
    name = models.CharField(_("نام و نام خانوادگی"),max_length=100)
    email = models.EmailField(_("آدرس الکترونیکی"),max_length=250)
    phone = models.CharField(_("تلفن"),max_length=20)
    number = models.IntegerField(_("تعداد"))
    date = models.DateField(_("تاریخ"),auto_now=False,auto_now_add=False)
    time = models.TimeField(_("ساعت"),auto_now=False,auto_now_add=False)

    class Meta:
        verbose_name = 'رزرو'
        verbose_name_plural = 'رزرو کردن '

    def __str__(self):
        return self.email