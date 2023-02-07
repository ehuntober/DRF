from django.shortcuts import render
from rest_framework import generics
# Create your views here.

from .models import Product
from .serializers import ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
 
product_create_view = ProductCreateAPIView.as_view() 

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    
    serializer_class = ProductSerializer
    
product_detail_view = ProductDetailAPIView.as_view()
    