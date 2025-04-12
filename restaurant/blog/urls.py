from django.urls import path # type: ignore
from .import views


app_name = "blog"

urlpatterns = [
    path('',views.blog_list,name="blog_list"),
    path('<int:id>',views.blog_detail,name="blog_detail"),
    path('tag/<slug:tag>',views.blog_tag,name="tag"),
    path('category/<slug:category>',views.blog_tag,name="category"),
    path('search/',views.search,name="search"),
]
