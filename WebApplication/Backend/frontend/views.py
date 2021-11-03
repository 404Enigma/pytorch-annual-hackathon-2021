from django.shortcuts import render
from rest_framework.response import Response
import matplotlib.pyplot as plt
import numpy as np
from . import process as pr
# Create your views here.



def home(request):
    
    img = pr.get_image()
    
    
    return render(request,'home.html',{})


def home2(request):
    
    with open(r'static/Images/Image_#76.png', 'rb') as f:
        im_b64 = (f.read())
        
    