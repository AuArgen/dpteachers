from django.db import models

from klass.models import Klass
from teacher.models import Teacher


class Klasssteacher(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Мугалим')
    klass = models.OneToOneField(Klass, on_delete=models.CASCADE, verbose_name='Класс', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Класс жетечи'
        verbose_name_plural = 'Класс жетечилер'

    def __str__(self):
        return f'{self.teacher.user.last_name} {self.teacher.user.first_name} {self.klass.title}'
