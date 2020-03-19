from django.contrib import admin
from .models import Post, Comment, Author


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('blogger', 'title', 'text', 'pub_date')
    list_filter = ('blogger', 'pub_date')
    inlines = [CommentInline]


admin.site.register(Author)
