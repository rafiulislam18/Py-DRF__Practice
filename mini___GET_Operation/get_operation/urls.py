from django.urls import path
from . import views


urlpatterns = [
    # API endpoints - GET all students and single student
    path('students/', views.student_list),
    path('students/<int:pk>', views.student_detail),
]
