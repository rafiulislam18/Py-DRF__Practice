from django.urls import path
from .views import StudentList


urlpatterns = [
    # API endpoint - GET all students, POST
    path('students/', StudentList.as_view(), name='student_list'),
]
