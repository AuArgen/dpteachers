from django.db import models

class Klass(models.Model):
    title = models.CharField(max_length=10, unique=True, verbose_name='Класстын аталышы')

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Класстар'
    def __str__(self):
        return self.title
