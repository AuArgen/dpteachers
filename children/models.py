import os
import uuid

from django.contrib.auth.models import User
from django.db import models

from klass.models import Klass

def generate_unique_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('media/child/avatars/', filename)
class Child(models.Model):
    child = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Окуучу тандоо')
    klass = models.ForeignKey(Klass, on_delete=models.CASCADE, verbose_name='Класс тандоо')
    avatar = models.ImageField(upload_to=generate_unique_filename, verbose_name='Сүрөтү')
    phone = models.CharField(max_length=20, verbose_name='Телефон номер')
    mother = models.CharField(max_length=100, verbose_name='Апасынын аты-жөнү')
    father = models.CharField(max_length=100, verbose_name='Атасынын аты-жөнү')
    address = models.CharField(max_length=250, verbose_name='Дареги')

    class Meta:
        verbose_name = 'Окуучу'
        verbose_name_plural = 'Окуучулар'

    def __str__(self):
        return f'{self.child.last_name} - {self.child.first_name} {self.klass} {self.mother} {self.father}'
