from django.contrib import admin
from .models import Post, Categories, about_us


class PostAdmin(admin.ModelAdmin):

    list_display = ("title", "content")
    search_fields = ("title", "content")
    list_filter = ("category", "created_at")

admin.site.register(Post, PostAdmin)
admin.site.register(Categories)
admin.site.register(about_us)
