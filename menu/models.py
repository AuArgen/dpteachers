from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Menu(models.Model):
    title=models.CharField(max_length=30, verbose_name='Главные меню')
    icon=models.ImageField(upload_to='media/%d/', verbose_name='Добавьте иконку для меню')
    description = RichTextField(verbose_name="Содержание")
    
    def __str__(self) -> str:
        return self.title
