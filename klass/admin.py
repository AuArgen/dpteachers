from django.contrib import admin
from .models import *

@admin.register(Klass)
class KlassAdmin(admin.ModelAdmin):
    list_display = ('title', )
