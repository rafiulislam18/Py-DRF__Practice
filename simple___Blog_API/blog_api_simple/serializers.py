from rest_framework import serializers
from .models import BlogPost


# Define serializer for BlogPost model
class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author']  # Instead we can use: '__all__'