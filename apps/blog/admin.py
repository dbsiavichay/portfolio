# Django
from django.contrib import admin

# Models
from apps.blog.models import Post, Media


@admin.register(Media)
class Mediadmin(admin.ModelAdmin):
    list_display = ('name', 'file_extension', 'date')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date',)
