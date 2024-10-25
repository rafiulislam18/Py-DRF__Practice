from django.contrib import admin
from .models import Medicine


# Register Medicine model in admin
@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'manufacturer', 'price']