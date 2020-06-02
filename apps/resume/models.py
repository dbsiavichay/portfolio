# Django
from django.db import models


class Timeline(models.Model):
    start_date = models.DateField(verbose_name='fecha de inicio')
    ends_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='fecha de finalización'
    )


class JobTitle(Timeline):
    level = models.CharField(
        max_length=64,
        verbose_name='nivel de instrucción'
    )
    institution = models.CharField(max_length=128, verbose_name='institución')
    name = models.CharField(
        max_length=128,
        verbose_name='título obtenido'
    )
    senescyt_number = models.CharField(
        max_length=64,
        blank=True,
        null=True,
        verbose_name='registro senescyt'
    )

    class Meta:
        verbose_name = 'título profesional'
        verbose_name_plural = 'títulos profesionales'

    def __str__(self):
        return f'{self.level} - {self.name}'


class JobExperience(Timeline):
    institution = models.CharField(max_length=128, verbose_name='institución')
    job_position = models.CharField(max_length=64, verbose_name='cargo/puesto')
    current_job = models.BooleanField(
        default=False,
        verbose_name='trabajo actual?'
    )

    class Meta:
        verbose_name = 'experiencia profesional'
        verbose_name_plural = 'experiencias profesionales'

    def __str__(self):
        return f'{self.job_position} - {self.institution}'


class JobActivity(models.Model):
    description = models.CharField(max_length=64, verbose_name='descripción')
    experience = models.ForeignKey(JobExperience, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'actividad'
        verbose_name_plural = 'actividades'
