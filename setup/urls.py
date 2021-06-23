from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static # media

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('image_text_detector.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # media
