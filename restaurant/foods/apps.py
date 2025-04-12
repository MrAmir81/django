from django.apps import AppConfig # type:ignore


class FoodsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'foods'
    verbose_name = "غذاها"
