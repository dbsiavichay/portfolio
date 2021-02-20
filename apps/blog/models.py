# Django
from django.db import models


class Media(models.Model):
    name = models.CharField(max_length=128, verbose_name='nombre')
    file = models.FileField(upload_to='files/%Y/%m/%d/')
    file_extension = models.CharField(max_length=32)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.name


class Post(models.Model):
    DRAFT, PUBLISHED = 1, 2
    STATE_CHOICES = (('Borrador', DRAFT), ('Publicado', PUBLISHED))

    title = models.CharField(max_length=128, verbose_name='título')
    cover = models.ImageField(
        upload_to='posts/%Y/%m/%d/',
        blank=True,
        null=True,
        verbose_name='portada'
    )
    date = models.DateTimeField(auto_now_add=True, verbose_name='fecha')
    content = models.TextField(verbose_name='contenido')
    state = models.PositiveSmallIntegerField(
        choices=STATE_CHOICES,
        default=DRAFT
    )

    def __str__(self):
        return self.title
