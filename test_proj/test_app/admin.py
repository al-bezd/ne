from django.contrib import admin

# Register your models here.
from models import BlogPost, Blog, BlogUser


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=(
        'title_blog',
    )
    list_display_links = (
        'title_blog',
    )
    pass
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display=(
        'title_post',
        'date_create',
    )
    list_display_links = (
        'title_post',
    )
    pass
@admin.register(BlogUser)
class BlogUserAdmin(admin.ModelAdmin):
    pass
