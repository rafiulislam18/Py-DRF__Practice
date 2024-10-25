from django.contrib import admin
from .models import Student


# Register Student model in admin with custom configuration
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'class_enrolled', 'date_of_birth')
    search_fields = ('first_name', 'last_name')
    list_filter = ('class_enrolled',)

    # Organize fields in fieldsets
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'date_of_birth')
        }),
        ('Class Information', {
            'fields': ('class_enrolled',)
        }),
    )
