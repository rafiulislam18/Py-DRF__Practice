from django.contrib import admin
from .models import Student

# Register Student model with custom admin configuration
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'class_enrolled', 'date_of_birth')
    search_fields = ('first_name', 'last_name')
    list_filter = ('class_enrolled',)
