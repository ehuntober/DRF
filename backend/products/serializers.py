from rest_framework import serializers

from .models import Product

class ProductForm(serializers.ModelSerializer()):
    class Meta:
        model = Product
        fields  =[
            'title',
            'content',
            'price',
            'sale_price',
            'get_discount'
        ]