from rest_framework import viewsets
from .models import Class
from .serializers import ClassSerializer
from permissions.permissions import CustomIsAdminOrReadOnly


# ViewSet for CRUD on Class model (admin or read-only)
class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [CustomIsAdminOrReadOnly]
