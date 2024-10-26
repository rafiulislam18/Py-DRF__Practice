from rest_framework import serializers
from .models import Class


# Define serializer for Class model
class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'
