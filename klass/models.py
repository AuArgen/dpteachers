from django.db import models

class Klass(models.Model):
    title = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return self.title
