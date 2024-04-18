from datetime import timezone

from django.db import models


class Saatar(models.Model):
    title = models.CharField(max_length=10, unique=True, verbose_name='Аталышы')
    saat_start = models.TimeField(verbose_name='Саат башталуу убактысы')
    saat_end = models.TimeField(verbose_name='Саат аяктоо убактысы')

    class Meta:
        verbose_name = 'Саат'
        verbose_name_plural = 'Сааттар'

    def __str__(self):
        return self.title