from rest_framework import generics
from .models import Attendance
from .serializers import AttendanceSerializer
from ..permissions.permissions import CustomIsAdminOrReadOnly


# API view to list & create Attendance records (is admin or read-only)
class AttendanceListCreate(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [CustomIsAdminOrReadOnly]


# API view to retrieve, update & delete any Attendance record (is admin or read-only)
class AttendanceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [CustomIsAdminOrReadOnly]
