from rest_framework import serializers
from .models import Student


# Define serializer for Student model
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'class_enrolled', 'date_of_birth']

    # Custom field validation for d.o.b
    def validate_date_of_birth(self, value):
        if value.year > 2018:
            raise serializers.ValidationError("Student must be older than 6.")
        return value
