from django.contrib import admin
from .models import *


@admin.register(Saatar)
class Admin(admin.ModelAdmin):
    list_display = ('title', 'saat')
