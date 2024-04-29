from django.contrib import admin
from .models import *

@admin.register(DocChild)
class DocChildAdmin(admin.ModelAdmin):
    list_display = ('get_first_name', 'title', 'description', 'doc')

    def get_first_name(self, obj):
        return f'{obj.child.child.last_name} {obj.child.child.first_name}' if obj.child.child else ''
