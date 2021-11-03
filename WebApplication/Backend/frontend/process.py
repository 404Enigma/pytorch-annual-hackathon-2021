import matplotlib.pyplot as plt
import base64
from io import BytesIO
import torch
from . import Mod2

def get_graph():
    
    buffer = BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    img_png = buffer.getvalue()
    graph = base64.b64encode(img_png)
    graph = graph.decode('utf-8')
    buffer.close()    
    return graph
        
        
def get_image():
    img = plt.imread('static/Images/Image_#76.png')
    return img


def Predict():
    pred = torch.load('static/Models/Model_1.2_epoch100')
    pass
