import os
import uuid
from django.db import models

from children.models import Child


def generate_unique_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('media/child/avatars/', filename)


class DocChild(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE, verbose_name='Окуучу тандоо ')
    doc = models.FileField(upload_to=generate_unique_filename, blank=True, null=True, verbose_name='Документ')
    title = models.CharField(max_length=100, default="Тема", verbose_name='Тема')
    description = models.TextField(default="Маалымат", verbose_name='Кошумча маалымат')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Кошумча маалымат'
        verbose_name_plural = 'Окуучу маалыматы'

    def __str__(self):
        return f' {self.child.child.first_name} {self.title} {self.description}'
