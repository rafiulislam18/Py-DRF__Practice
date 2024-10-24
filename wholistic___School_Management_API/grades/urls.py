from rest_framework.routers import DefaultRouter
from .views import GradeViewSet


# Configure URL route for GradeViewSet
router = DefaultRouter()
router.register(r'grades', GradeViewSet)

urlpatterns = router.urls
