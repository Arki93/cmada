
from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

        read_only_fields = (
            'created_by',
            'modified_by',
        ),
        fields = (
            'id',
            'product_id',
            'product_name',
            'product_unit_price',
            'product_type',
            'on_going_command',
            'minimun_stock',
            'tva',
        )

