from django.contrib import admin
from .models import Blog, BlogComment, BlogCategory, BlogLikes
# Register your models here.
admin.site.register(Blog)
admin.site.register(BlogComment)
admin.site.register(BlogCategory)
admin.site.register(BlogLikes)

class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'content']}),
    ]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'blog', 'content', 'created_at')
    list_filter = ('user', 'blog')
    search_fields = ('user', 'blog')
    ordering = ('-created_at',)

