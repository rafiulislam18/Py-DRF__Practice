from django.urls import path
from . import views


urlpatterns = [
    # API endpoint - GET (all), POST on Teacher model
    path('', views.teacher_list_create, name='teacher_list'),
]
