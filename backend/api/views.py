from django.shortcuts import render

# Create your views here.
#

import json
from django.http import JsonResponse

def api_home(request,*args,**kwargs):
    body = request.body # byte string of JSON data
    data ={}
    try:
        data = json.loads(body)
    
    except:
        pass
    print(data)
    data['header'] = request.headers
    data['content_type'] = request.content_type
    
    return JsonResponse({
        "message": "Hi there, this is your DJango API response"
    })
