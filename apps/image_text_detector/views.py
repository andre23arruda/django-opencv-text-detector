from django.shortcuts import render
from .forms import ImageInputForms
from image_text_detector.utils import process_image

import matplotlib.pyplot as plt
import io
import urllib, base64
import numpy as np

# Agg para renderizar imagem
from matplotlib import use
use('Agg')

def get_image(image):
    '''Retorna endereço da imagem'''
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri =  urllib.parse.quote(string)
    return uri


def text_detector(request):
    '''Página para submeter imagem'''
    images  = {}

    if request.method == 'POST':
        if 'image' in request.FILES:
            image = request.FILES['image']
            result = process_image.get_image_text(image)

            images['original'] =  get_image(result[0])
            images['with_box'] =  get_image(result[1])

    form = ImageInputForms()


    context = {
        'page_title': 'Text Detector',
        'form': form,
        'images': images,
    }

    return render(request, 'image_text_detector/text_detector.html', context)