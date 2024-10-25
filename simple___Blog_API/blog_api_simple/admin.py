from django.contrib import admin
from .models import BlogPost


# Register BlogPost model in admin
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'author')