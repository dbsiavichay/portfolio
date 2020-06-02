# Django
from django.db import models


class Timeline(models.Model):
    start_date = models.DateField()
    ends_date = models.DateField(null=True)


class JobTitle(Timeline):
    level = models.CharField(max_length=64)
    name = models.CharField(max_length=128)
    institution = models.CharField(max_length=128)
    senescyt_number = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return f'{self.level} - {self.name}'


class JobExperience(Timeline):
    job_position = models.CharField(max_length=64)
    institution = models.CharField(max_length=128)
    current_job = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.job_position} at {self.institution}'


class JobActivity(models.Model):
    description = models.TextField()
    experience = models.ForeignKey(JobExperience, on_delete=models.CASCADE)
