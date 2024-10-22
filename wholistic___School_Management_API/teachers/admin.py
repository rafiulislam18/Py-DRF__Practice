from django.contrib import admin
from .models import Teacher


# Register Teacher model with custom admin configuration
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'subject']
    search_fields = ['first_name', 'last_name', 'subject']
    list_filter = ['subject']
