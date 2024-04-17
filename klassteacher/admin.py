from django.contrib import admin
from .models import *


@admin.register(Klasssteacher)
class Admin(admin.ModelAdmin):
    list_display = ('teacher', 'klass')
