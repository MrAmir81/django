from django.db import models # type:ignore
from django.utils.translation import gettext as _ # type:ignore


class Food(models.Model):
    FOOD_TYPE=[
        ('breakefast','صبحانه'),
        ('drinks','نوشیدنی'),
        ('dinner','شام'),
        ('lunch','ناهار')
    ]
    name = models.CharField(_("نام غذا"),max_length=100)
    description = models.CharField(_("توضیحات"),max_length=100)
    rate = models.IntegerField(_("امتیاز"))
    price = models.IntegerField(_("قیمت"))
    time = models.IntegerField(_("زمان لازم"))
    pub_date = models.DateField(_("تاریخ انتشار"), auto_now=False, auto_now_add=True)
    photo = models.ImageField(_("عکس"), upload_to='foods/')
    type_food = models.CharField(_("نوع غذا"),choices=FOOD_TYPE,max_length=10,default='drinks')

    class Meta:
        verbose_name = 'غذا'
        verbose_name_plural = 'غذاها'


    def __str__(self):
        return self.name