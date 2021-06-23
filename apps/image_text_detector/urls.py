from django.urls import path
from .views import *

urlpatterns = [
    path('', text_detector, name='text_detector'),
]