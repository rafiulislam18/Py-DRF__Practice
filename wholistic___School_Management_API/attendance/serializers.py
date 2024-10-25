from rest_framework import serializers
from .models import Attendance


# Define serializer for Attendance model
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
