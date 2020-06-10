from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name='nombre')

    class Meta:
        verbose_name = 'categoría'

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=128, verbose_name='nombre')
    description = models.TextField(verbose_name='descripción')
    image = models.ImageField(upload_to='projects')
    url = models.URLField()
    date = models.DateField(verbose_name='fecha')
    categories = models.ManyToManyField(
        Category,
        verbose_name='categorías'
    )

    class Meta:
        ordering = ('date',)
        verbose_name = 'proyecto'

    def __str__(self):
        return self.name
