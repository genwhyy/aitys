from django.urls import path
from .views import register, home, user_login, profile_edit, profile
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('register/', register, name='register'),
    path('home/', home, name='home'),
    path('login/', user_login, name='user_login'),
    path('edit/', profile_edit, name='profile_edit'),
    path('profile/', profile, name='profile')
]

if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL,
 document_root=settings.MEDIA_ROOT)