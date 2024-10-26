from django.urls import path
from .views import AttendanceListCreate, AttendanceDetail


urlpatterns = [
    # API endpoints - CRUD on Attendance
    path('', AttendanceListCreate.as_view(), name='attendance_list_create'),
    path('<int:pk>/', AttendanceDetail.as_view(), name='attendance_detail'),
]
