from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
import json
import base64
# Create your views here.



class MRImage(APIView):
    
    def post(self,request):
        print('!!!!!!!!!!!!!!!!!!! Called !!!!!!!!!!!!!!!!!!! : ',request.method,request)
        if request.method =='POST':
            #post.file
            #print('MMMMM : ',self.request.POST)
            #print('NNNN : ',request.POST.items())
            dict_obj = json.load(request)#request.files.get('file')#json.load(request)
            #im = dict_obj['img']
            # img = base64.b64decode(im)
            
            print('LLAAOA : ',dict_obj)
        return JsonResponse({'status':'200'})