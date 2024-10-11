from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicineViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



router = DefaultRouter()
router.register(r'medicines', MedicineViewSet)



schema_view = get_schema_view(
    openapi.Info(
        title="Medicine API (Simple)",
        default_version='v1'
    ),
    public=True,
)


# urlpatterns = router.urls


urlpatterns = [
    path('', include(router.urls)),
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
]