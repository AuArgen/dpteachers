import os
import uuid

from django.db import models

def generate_unique_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('media/news/avatars/', filename)

class News(models.Model):
    doc = models.FileField(upload_to=generate_unique_filename, blank=True, null=True, verbose_name='Документ')
    image = models.ImageField(upload_to=generate_unique_filename, verbose_name='Cүрөт')
    title = models.CharField(max_length=100, default="Тема", verbose_name='Тема')
    description = models.TextField( default="Маалымат", verbose_name='Кошумча маалымат')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Жаңылык'
        verbose_name_plural = 'Жаңылыктар'

    def __str__(self):
        return f'  {self.title} {self.description} {self.image} {self.doc}'