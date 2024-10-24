from rest_framework import serializers
from .models import Grade


# Implement serializer for Grade model
class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'
