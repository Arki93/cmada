from rest_framework import serializers
from .models import Invoice, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        read_only_fields = (
            'invoice',
        )  # 'invoice' should be read-only in the serializer
        fields = (
            'id',
            'item_id',  # Correct field name
            'item_name',
            'quantity',
            'unit_price',
            'total',
            'tva',
            'item_reduction',
            'item_num',
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
        )
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
            'client_ville',
            'invoice_type',
            'due_date', 
            'is_sent',
            'total_ht', 
            'total_tva',
            'tva_5',
            'tva_20',   
            'total_ttc', 
            'invoice_reduction',
            'client',
            'is_paid',
            'items',
        )

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        invoice = Invoice.objects.create(**validated_data)

        for item_data in items_data:
            Item.objects.create(invoice=invoice, **item_data)

        return invoice
    
    def update(self, instance, validated_data):
        items_data = validated_data.pop('items', [])

        # Update the invoice instance
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Handle items
        current_item_ids = [item.id for item in instance.items.all()]
        new_item_ids = [item_data.get('id') for item_data in items_data]

        # Delete items that are no longer in the request
        for item_id in current_item_ids:
            if item_id not in new_item_ids:
                Item.objects.filter(id=item_id).delete()

        # Update or create items
        for item_data in items_data:
            item_id = item_data.get('id')
            if item_id:
                item = Item.objects.get(id=item_id)
                for attr, value in item_data.items():
                    setattr(item, attr, value)
                item.save()
            else:
                Item.objects.create(invoice=instance, **item_data)

        return instance
