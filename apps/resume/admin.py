# Django
from django.contrib import admin

# Models
from apps.resume.models import JobTitle, JobExperience, JobActivity


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
