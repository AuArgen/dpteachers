from django.contrib import admin

from teacher.models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('get_first_name', 'phone')

    def get_first_name(self, obj):
        return f'{obj.user.last_name} {obj.user.first_name}' if obj.user else ''
