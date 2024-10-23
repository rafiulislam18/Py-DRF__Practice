from django.contrib import admin
from .models import Grade


# Register Grade model with custom admin configuration
@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'score')
    search_fields = ('student__first_name', 'student__last_name', 'subject')
    list_filter = ('subject', 'score')
