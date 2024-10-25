from django.urls import path
from . import views


urlpatterns = [
    # API endpoint - POST (create) student
    path('students/', views.student_create),
]
