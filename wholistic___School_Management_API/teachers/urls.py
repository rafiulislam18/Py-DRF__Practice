from django.urls import path
from . import views

urlpatterns = [
    # API endpoint - GET teacher list
    path('', views.teacher_list, name='teacher_list'),
]
