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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    predmet = models.ForeignKey(Predmet, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to=generate_unique_filename)

    def __str__(self):
        return f' {self.user.first_name} {self.user.last_name}'