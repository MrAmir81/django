from django.urls import path # type: ignore 
from .import views


app_name = "foods"

urlpatterns = [
    path("",views.food_list,name='food_list'),
    path("<int:id>/",views.food_detail,name="detail")
]