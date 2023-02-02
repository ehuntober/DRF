from django.shortcuts import render

# Create your views here.
#

import json
from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

@api_view
def api_home(request,*args,**kwargs):
    
    """
    DRF API VIEW
    """
    # model_data = Product.objects.all().order_by("?").first()
    instance = Product.objects.all().order_by("?").first()
    data = {}
    # if model_data:
        # data = model_to_dict(model_data, fields=['id','title','price', 'sale_price'])
        # data['id']= model_data.id
        # data['title']= model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        
    if instance:
        data = ProductSerializer(instance).data
        
    return Response(data)





# def api_home(request,*args,**kwargs):
#     body = request.body # byte string of JSON data
#     data ={}
#     try:
#         data = json.loads(body)
    
#     except:
#         pass
#     print(data)
#     data['header'] = request.headers
#     data['content_type'] = request.content_type
    
#     return JsonResponse({
#         "message": "Hi there, this is your DJango API response"
#     })
