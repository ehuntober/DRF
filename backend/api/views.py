from django.shortcuts import render

# Create your views here.
#

import json
from django.http import JsonResponse\

from products.models import Product

def api_home(request,*args,**kwargs):
    model_data = Product.object.all().order_by("?").first()
    data = {}
    if model_data:
        data['title']= model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
        
    return JsonResponse(data)





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
