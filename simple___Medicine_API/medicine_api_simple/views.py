from rest_framework import viewsets
from .models import Medicine
from .serializers import MedicineSerializer


# ViewSet for handling CRUD on Medicine model
class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
