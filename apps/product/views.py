from django.shortcuts import render
    
from rest_framework import viewsets

from .serializers import ProductSerializer
from .models import Product

from django.core.exceptions import PermissionDenied

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, modified_by=self.request.user)

    def perform_update(self, serializer):
        obj = self.get_object()

        if self.request.user != obj.created_by:
            raise PermissionDenied('Suppression Impossible!')

        serializer.save()