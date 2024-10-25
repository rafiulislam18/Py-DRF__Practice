from django.urls import path
from . import views


urlpatterns = [
    # API endpoint - GET all teachers
    path('', views.teacher_list_create, name='teacher_list'),
]
