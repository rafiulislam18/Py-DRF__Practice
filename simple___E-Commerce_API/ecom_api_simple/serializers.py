from rest_framework import serializers
from .models import Product


# Define serializer for Product model
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']  # Instead we can use: '__all__'