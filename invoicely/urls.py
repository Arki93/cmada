from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.urls import path

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path("admin/", admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('apps.client.urls')),
    path('api/v1/', include('apps.team.urls')),
    path('api/v1/', include('apps.invoice.urls')),
    path('api/v1/', include('apps.product.urls')),
    path('api/v1/', include('apps.stock.urls')),
]
