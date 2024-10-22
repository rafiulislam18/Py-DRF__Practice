from rest_framework import serializers
from .models import Teacher


# Define serializer for Teacher model
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
