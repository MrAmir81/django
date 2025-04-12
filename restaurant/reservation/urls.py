from django.urls import path #type:ignore
from . import views

app_name = "reservation"

urlpatterns = [
    path('',views.reserve,name="reserve")
]