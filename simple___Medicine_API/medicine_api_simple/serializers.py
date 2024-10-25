from rest_framework import serializers
from .models import Medicine


# Define serializer for Medicine model
class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ['id', 'name', 'manufacturer', 'price']  # Instead we can use: '__all__'
