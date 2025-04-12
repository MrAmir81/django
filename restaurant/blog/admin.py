from django.contrib import admin # type: ignore
from .models import Blog , Category , Tag , Comments

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comments)

class BlogAdmin(admin.ModelAdmin):
   list_display = ("title","created_at")
   list_filter = ("author","category",)
   search_fields = ("title",)
   
admin.site.register(Blog,BlogAdmin)
