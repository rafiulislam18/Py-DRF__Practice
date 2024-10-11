from django.urls import path
from .views import ProductList, ProductDetail
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="E-Commerce API (Simple)",
        default_version='v1'
    ),
    public=True,
)

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
]
