from rest_framework import viewsets
from .models import Class
from .serializers import ClassSerializer
from permissions.permissions import CustomIsAdminOrReadOnly  # Assuming custom permission as an example


# ViewSet for CRUD on Class model
class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [CustomIsAdminOrReadOnly]  # Optional: set custom permission for admin-only write access
