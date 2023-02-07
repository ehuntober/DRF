from django.shortcuts import render
from django
# Create your views here.

from .models import Product
from .serializers import ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    
    serializer_class = ProductSerializer
    
product_detail_view = ProductDetailAPIView.as_view()
    