from django.contrib import admin

from raspisanie.models import Raspisanie


@admin.register(Raspisanie)
class RaspisanieAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher', 'predmet', 'klass', 'saat')
