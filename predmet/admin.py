from django.contrib import admin
from .models import *

@admin.register(Predmet)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('title',)
