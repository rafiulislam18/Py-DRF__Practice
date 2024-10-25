from rest_framework import viewsets
from .models import Grade
from .serializers import GradeSerializer


# ViewSet for CRUD on Grade model
class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
