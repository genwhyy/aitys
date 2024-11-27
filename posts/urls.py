from django.urls import path
from .views import dashboard, create_post
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/', create_post, name='dashboard'),
]

if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL,
 document_root=settings.MEDIA_ROOT)