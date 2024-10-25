from django.urls import path
from .views import ProductListCreate, ProductDetail


urlpatterns = [
    # API endpoints - CRUD on Product model
    path('products/', ProductListCreate.as_view(), name='product_list_create'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
]
