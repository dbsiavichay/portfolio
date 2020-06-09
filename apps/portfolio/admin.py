# Django
from django.contrib import admin

# Models
from apps.portfolio.models import Category, Project


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'date', 'category')
