from django.db import models


class Saatar(models.Model):
    title = models.CharField(max_length=10, unique=True, verbose_name='Аталышы')
    saat = models.TimeField(verbose_name='Сааты')

    class Meta:
        verbose_name = 'Саат'
        verbose_name_plural = 'Сааттар'

    def __str__(self):
        return self.title