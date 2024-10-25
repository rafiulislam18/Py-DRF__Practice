from django.contrib import admin
from .models import Student


# Register Student model in admin
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']