from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination




class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']
    pagination_class = PageNumberPagination



class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

