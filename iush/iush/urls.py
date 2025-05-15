"""
URL configuration for iush project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.http import HttpResponse
from django.contrib import admin
from rest_framework import permissions # Importa esto
from drf_yasg.views import get_schema_view # Importa esto
from drf_yasg import openapi # Importa esto
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


schema_view = get_schema_view(
    openapi.Info(
        title="Tu API Django",
        default_version='v1',
        description="Documentación de la API de tu proyecto",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

def test_view(request):
    return HttpResponse("Hola Django!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('vocacional.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), # Agrega esto
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), # Agrega esto
    path('', test_view, name='test'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)