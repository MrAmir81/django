from django.urls import path # type: ignore 
from .import views

app_name = "contact"

urlpatterns = [
    path("",views.contact,name="contact")
]
