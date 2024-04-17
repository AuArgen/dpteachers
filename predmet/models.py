from django.db import models


class Predmet(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Предмет аталышы')

    class Meta:
        verbose_name = 'Передмет'
        verbose_name_plural = 'Предметтер'

    def __str__(self):
        return self.title
