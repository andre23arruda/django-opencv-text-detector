from PIL import Image
import numpy as np
from .text_detection import cv2_text_detection


def get_image_text(image):
    '''Processa imagem e encontra textos'''
    # abre com PIL e converte para np array
    image = (np.array(Image.open(image))).astype('uint8')
    if len(image.shape) > 2:
        image = image[:, :, :3]
    elif len(image.shape) == 2:
        image = np.stack((image, image, image), axis=2)
    images = cv2_text_detection(image)

    return images