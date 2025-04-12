from django.apps import AppConfig #type:ignore


class ContactConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact'
    verbose_name = "مخاطب"
