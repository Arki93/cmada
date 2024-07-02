from typing_extensions import Required
from rest_framework import serializers

from .models import Invoice, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        read_only_fields = (
            'invoice',
        )
        fields = (
            'id',
            'item_id',
            'item_name',
            'quantity',
            'unit_price',
            'total',
            'tva',
            'reduction',
        )


class InvoiceSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Invoice
        read_only_fields = (
            'created_at',
            'created_by',
            'modified_by',
            'modified_at',
            'team',
        ),

        fields = (
            'id',
            'created_at',
            'invoice_number',
            'client_name',
            'client_email', 
            'client_siret',
            'client_address',
            'client_cp',
            'client_pays', 
            'invoice_type',
            'due_date', 
            'is_sent',
            'total_ht', 
            'total_tva',
            'tva_5',
            'tva_20',   
            'total_ttc', 
            'reduction',
            'client',
            'is_paid',
            'items',
        )

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        invoice = Invoice.objects.create(**validated_data)

        for item in items_data:
            Item.objects.create(invoice=invoice, **item)

        return invoice