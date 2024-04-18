from django.db import models
from klass.models import Klass
from predmet.models import Predmet
from saatar.models import Saatar
from teacher.models import Teacher

DAYS_OF_WEEK = [
    ('Понедельник', 'Понедельник'),
    ('Вторник', 'Вторник'),
    ('Среда', 'Среда'),
    ('Четверг', 'Четверг'),
    ('Пятница', 'Пятница'),
    ('Суббота', 'Суббота'),
    ('Воскресенье', 'Воскресенье'),
]

class Raspisanie(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Мугалим')
    predmet = models.ForeignKey(Predmet, on_delete=models.CASCADE, verbose_name='Сабак')
    klass = models.ForeignKey(Klass, on_delete=models.CASCADE, verbose_name='Класс')
    saat = models.ForeignKey(Saatar, on_delete=models.CASCADE, verbose_name='Саат')
    day = models.CharField(max_length=20, choices=DAYS_OF_WEEK, verbose_name='День недели')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Жадыбал'
        verbose_name_plural = 'Жадыбалдар'

    def __str__(self):
        return f'{self.day} - {self.teacher} - {self.klass} - {self.predmet} - {self.saat}'
