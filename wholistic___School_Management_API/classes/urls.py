from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClassViewSet


# Configure URL route for ClassViewSet
router = DefaultRouter()
router.register(r'', ClassViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
