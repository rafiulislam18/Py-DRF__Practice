from django.urls import path
from .views import StudentList


urlpatterns = [
    # API endpoint - POST, GET all students
    path('students/', StudentList.as_view(), name='student_list'),
]