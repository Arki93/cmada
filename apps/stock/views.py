from django.shortcuts import render

from rest_framework import viewsets

from .serializers import StockSerializer, ProductStockSerializer, ProductStockArchiveSerializer
from .models import Stock, ProductStock, ProductStockArchive

from django.core.exceptions import PermissionDenied

class StockViewSet(viewsets.ModelViewSet):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()

    def perform_create(self, serializer):
        team = self.request.user.teams.first()
        serializer.save(created_by=self.request.user, modified_by=self.request.user)

    def perform_update(self, serializer):
        obj = self.get_object()
    
class ProductStockViewSet(viewsets.ModelViewSet):
    serializer_class = ProductStockSerializer
    queryset = ProductStock.objects.all()
    
class ProductStockArchiveViewSet(viewsets.ModelViewSet):
    serializer_class = ProductStockArchiveSerializer
    queryset = ProductStockArchive.objects.all()