from django.contrib import admin
from .models import Class


# Register Class model in admin
@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
