from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

def home(request):
    return JsonResponse({
        'message': 'Bienvenue sur l\'API',
        'endpoints': {
            'users': '/api/users/',
            'login': '/api/login/',
            'admin': '/admin/',
        }
    })

urlpatterns = [
    path('', home, name='home'),  # Vue d'accueil
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] 