from django.contrib import admin
from .models import Class


# Register Class model in admin
@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Display these fields in the list view
    search_fields = ('name',)  # Enable searching by name
