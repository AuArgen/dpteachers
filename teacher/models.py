from django.contrib.auth.models import User
from django.db import models
import os
import uuid

from predmet.models import Predmet


def generate_unique_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('media/teacher/avatars/', filename)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Мугалимдер')
    predmet = models.ForeignKey(Predmet, on_delete=models.CASCADE, verbose_name='Предмет тандоо')
    phone = models.CharField(max_length=12, unique=True, verbose_name='Телефон номери')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Кошулган убакыт')
    avatar = models.ImageField(upload_to=generate_unique_filename, verbose_name='Сүрөтү')

    class Meta:
        verbose_name = 'Мугалим'
        verbose_name_plural = 'Мугалимдер'

    def __str__(self):
        return f' {self.user.first_name} {self.user.last_name}'