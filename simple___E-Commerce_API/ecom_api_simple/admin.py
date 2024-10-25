from django.contrib import admin
from .models import Product


# Register Product model in admin
@admin.register(Product)
class ProducAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price')