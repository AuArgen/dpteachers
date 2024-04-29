from django.contrib import admin

from children.models import Child


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_first_name', 'klass', 'phone', 'address')
    list_filter = ('klass', 'address')
    search_fields = ('klass', 'get_first_name')
    def get_first_name(self, obj):
        return f'{obj.child.last_name} {obj.child.first_name}' if obj.child else ''
