from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import StockViewSet, ProductStockViewSet, ProductStockArchiveViewSet

router = DefaultRouter()
router.register('stock', StockViewSet, basename='stock')
router.register('stock_products', ProductStockViewSet, basename='stock_products')
router.register('stock_products_archive', ProductStockArchiveViewSet, basename='stock_products_archive')

urlpatterns = [
    path('', include(router.urls)),
]
