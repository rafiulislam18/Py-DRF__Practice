from django.urls import path
from . import views


urlpatterns = [
    path('stuinfo/', views.student_list),
    path('stuinfo/<int:pk>', views.student_detail),
]
