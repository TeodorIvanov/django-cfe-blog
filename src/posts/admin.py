from django.contrib import admin
from posts.models import Post
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "timestamp", "updated"]
    list_display_links = ["timestamp"]
    list_filter = ["timestamp", "updated"]
    search_fields = ["content", "title"]
    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)
