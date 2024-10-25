from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    # API endpoints - CRUD on BlogPost model
    path('blogs/', views.blog_list_create, name='blog_list_create'),
    path('blogs/<int:pk>/', views.blog_detail, name='blog_detail'),

    # JWT authentication endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
