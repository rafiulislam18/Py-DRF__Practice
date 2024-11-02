from django.urls import path
from . import views


urlpatterns = [
    # API endpoints - CRUD on Grade model
    path('', views.GradeListCreateView.as_view(), name='grade_list_create'),
    path('<int:pk>/', views.GradeDetailView.as_view(), name='grade_detail'),
]
