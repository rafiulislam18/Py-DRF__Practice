from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Attendance
from .serializers import AttendanceSerializer
from permissions.permissions import CustomIsAdminOrReadOnly


# API view to list & create Attendance records (is admin or read-only, paginated list response)
class AttendanceListCreate(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [CustomIsAdminOrReadOnly]
    pagination_class = PageNumberPagination


# API view to retrieve, update & delete any Attendance record (is admin or read-only)
class AttendanceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [CustomIsAdminOrReadOnly]
