from rest_framework import generics
from .models import Attendance
from .serializers import AttendanceSerializer

# API view to list & create Attendance records
class AttendanceListCreate(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

# API view to retrieve, update & delete Attendance records
class AttendanceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
