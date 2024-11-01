from django.urls import path
from .views import GradeView

urlpatterns = [
    # API endpoint - CRUD on Grade model
    path('grades/', GradeView.as_view(), name='grade_list_create'),
    path('grades/<int:pk>/', GradeView.as_view(), name='grade_detail'),
]
