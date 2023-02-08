from django.shortcuts import render
from rest_framework import generics
# Create your views here.

from .models import Product
from .serializers import ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self,serializer):
        #serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        
        serializer.save(content=content)
 
product_create_view = ProductCreateAPIView.as_view() 

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    
    serializer_class = ProductSerializer
    
product_detail_view = ProductDetailAPIView.as_view()

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    
    serializer_class = ProductSerializer
    
product_detail_view = ProductDetailAPIView.as_view()
    