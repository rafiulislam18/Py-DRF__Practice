from django.contrib import admin
from .models import Attendance


# Register the Attendance model with custom admin configurations
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'date', 'present']
    search_fields = ['student__first_name', 'student__last_name', 'date']
    list_filter = ['present', 'date']
