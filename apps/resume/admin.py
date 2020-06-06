# Django
from django.contrib import admin

# Models
from apps.resume.models import (
    JobTitle, JobExperience, JobActivity, Skill, Language
)


@admin.register(JobTitle)
class JobTitleAdmin(admin.ModelAdmin):
    list_display = ('level', 'institution', 'name')
    fields = (
        'level',
        'institution',
        'name',
        'senescyt_number',
        'start_date',
        'ends_date'
    )


class JobActivityInline(admin.TabularInline):
    model = JobActivity


@admin.register(JobExperience)
class JobExperienceAdmin(admin.ModelAdmin):
    list_display = ('institution', 'job_position', 'current_job')
    fields = (
        'institution',
        'job_position',
        'start_date',
        'ends_date',
        'current_job'
    )
    inlines = (
        JobActivityInline,
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'percent', 'order')
    list_editable = ('percent', 'order')


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'percent', 'order')
    list_editable = ('percent', 'order')
