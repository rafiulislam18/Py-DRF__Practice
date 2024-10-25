from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicineViewSet


# Configure URL route for MedicineViewSet
router = DefaultRouter()
router.register(r'medicines', MedicineViewSet)

urlpatterns = [
    path('', include(router.urls)),    
]

"""
Instead we can use: 
urlpatterns = router.urls
"""