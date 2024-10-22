from django.contrib import admin
from .models import Teacher


# Register Teacher model in admin with custom configuration
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'subject']
    search_fields = ['first_name', 'last_name', 'subject']
    list_filter = ['subject']
